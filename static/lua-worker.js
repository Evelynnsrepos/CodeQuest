// Runs Lua lessons with wasmoon (Lua 5.4 compiled to WebAssembly), off the main thread.
import { LuaFactory } from "/vendor/wasmoon.js";

const factory = new LuaFactory("/vendor/wasmoon-glue.wasm");

const HARNESS = `
local out = {}
local function capture(...)
  local parts = table.pack(...)
  for i = 1, parts.n do parts[i] = tostring(parts[i]) end
  out[#out + 1] = table.concat(parts, "\\t", 1, parts.n) .. "\\n"
end
print = capture
io.write = function(...)
  for _, v in ipairs({...}) do out[#out + 1] = tostring(v) end
end
io.read = function() error("io.read() isn't available in lessons. Set the value in your code instead.", 0) end

local result = {}
if __cq_prelude then
  -- Hidden setup code a course provides, such as a practice version of an API.
  local setup, setupErr = load(__cq_prelude, "=prelude.lua", "t")
  if not setup then
    result.error, result.output = "The course setup has an error: " .. setupErr, ""
    return result
  end
  setup()
end
local fn, err = load(__cq_code, "=main.lua", "t")
if not fn then
  result.error = err
  result.output = ""
  return result
end
local ok, runErr = pcall(fn)
if ok and type(_cq_after) == "function" then
  -- A course can print a summary of what the learner's code did.
  local afterOk, afterErr = pcall(_cq_after)
  if not afterOk then out[#out + 1] = "(summary failed: " .. tostring(afterErr) .. ")\\n" end
end
result.output = table.concat(out)
if not ok then result.error = tostring(runErr) end

if __cq_mode == "submit" and __cq_check and ok then
  output = result.output
  local check, checkErr = load(__cq_check, "=check.lua", "t")
  if not check then
    result.check_ok, result.check_msg = false, "The lesson's check has an error: " .. checkErr
  else
    local passed, msg = pcall(check)
    result.check_ok = passed
    if not passed then result.check_msg = (tostring(msg):gsub("^check%.lua:%d+: ", "")) end
  end
end
return result
`;

const norm = (s) => s.trim().split("\n").map((l) => l.trimEnd()).join("\n");

factory.getLuaModule().then(() => self.postMessage({ type: "ready" }),
  (err) => self.postMessage({ type: "failed", error: String(err) }));

self.onmessage = async (event) => {
  const { id, code, check, expected, prelude, mode } = event.data;
  let lua;
  try {
    lua = await factory.createEngine();
    lua.global.set("__cq_code", code);
    lua.global.set("__cq_check", check || undefined);
    lua.global.set("__cq_mode", mode);
    lua.global.set("__cq_prelude", prelude || undefined);
    const raw = await lua.doString(HARNESS);
    const result = { output: raw.output || "", error: raw.error || null };
    if (mode === "submit") {
      result.passed = true;
      result.message = "";
      if (result.error) {
        Object.assign(result, { passed: false, message: "Your program stopped with an error." });
      } else if (expected != null && norm(result.output) !== norm(expected)) {
        Object.assign(result, { passed: false, message: "The output doesn't match yet.", expected: expected.trim() });
      } else if (check && !raw.check_ok) {
        Object.assign(result, { passed: false, message: raw.check_msg || "Not quite yet." });
      }
    }
    self.postMessage({ type: "result", id, result });
  } catch (err) {
    self.postMessage({ type: "result", id, result: { output: "", error: String(err), passed: false } });
  } finally {
    lua?.global.close();
  }
};
