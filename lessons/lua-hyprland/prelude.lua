-- A practice copy of Hyprland's Lua config API (hyprland.lua, Hyprland 0.55+).
-- It doesn't change any real settings: it records every call so lessons can check them,
-- and prints a summary of what Hyprland would apply. Function names follow
-- Hyprland's example config: https://github.com/hyprwm/Hyprland/blob/main/example/hyprland.lua

local state = {
  config = {}, binds = {}, monitors = {}, env = {}, handlers = {}, execs = {},
  window_rules = {}, workspace_rules = {}, layer_rules = {}, curves = {}, animations = {},
  gestures = {}, devices = {}, permissions = {}, started = false,
}

local function strict(name, t)
  return setmetatable(t, {
    __index = function(_, key)
      error(("%s.%s isn't part of Hyprland's Lua API. Check the spelling."):format(name, tostring(key)), 2)
    end,
  })
end

local function is_list(t)
  return type(t) == "table" and (#t > 0 or next(t) == nil)
end

local function merge(dst, src)
  for k, v in pairs(src) do
    if type(v) == "table" and not is_list(v) and type(dst[k]) == "table" then
      merge(dst[k], v)
    else
      dst[k] = v
    end
  end
end

local function handle(record)
  record.enabled = true
  function record:set_enabled(on) self.enabled = on end
  return record
end

local function need_table(fn, value, example)
  if type(value) ~= "table" then
    error(("%s expects a table, like %s"):format(fn, example), 3)
  end
end

-- Dispatchers describe an action. They don't run anything until a key is pressed.
local function dispatcher(name)
  return function(args) return { dispatcher = name, args = args } end
end

local dsp = strict("hl.dsp", {
  exec_cmd = function(cmd)
    if type(cmd) ~= "string" then error("hl.dsp.exec_cmd expects a command string, like hl.dsp.exec_cmd(\"kitty\")", 2) end
    return { dispatcher = "exec_cmd", args = cmd }
  end,
  focus = dispatcher("focus"),
  layout = dispatcher("layout"),
  exit = dispatcher("exit"),
  window = strict("hl.dsp.window", {
    close = dispatcher("window.close"),
    float = dispatcher("window.float"),
    pseudo = dispatcher("window.pseudo"),
    move = dispatcher("window.move"),
    drag = dispatcher("window.drag"),
    resize = dispatcher("window.resize"),
    fullscreen = dispatcher("window.fullscreen"),
  }),
  workspace = strict("hl.dsp.workspace", {
    toggle_special = dispatcher("workspace.toggle_special"),
  }),
})

hl = strict("hl", {
  dsp = dsp,
  config = function(t)
    need_table("hl.config", t, "hl.config({ general = { gaps_in = 5 } })")
    merge(state.config, t)
  end,
  bind = function(keys, action, opts)
    if type(keys) ~= "string" then error("hl.bind needs the keys as a string first, like \"SUPER + Q\"", 2) end
    if type(action) ~= "table" or not action.dispatcher then
      error("The second argument to hl.bind should be a dispatcher, like hl.dsp.exec_cmd(\"kitty\")", 2)
    end
    local b = handle({ keys = keys, action = action, opts = opts or {} })
    state.binds[#state.binds + 1] = b
    return b
  end,
  monitor = function(t)
    need_table("hl.monitor", t, "hl.monitor({ output = \"\", mode = \"preferred\", position = \"auto\", scale = \"auto\" })")
    state.monitors[#state.monitors + 1] = t
  end,
  env = function(name, value) state.env[name] = value end,
  on = function(event, fn)
    if type(fn) ~= "function" then error("hl.on needs a function as its second argument", 2) end
    state.handlers[event] = state.handlers[event] or {}
    table.insert(state.handlers[event], fn)
  end,
  exec_cmd = function(cmd) state.execs[#state.execs + 1] = cmd end,
  window_rule = function(t)
    need_table("hl.window_rule", t, "hl.window_rule({ name = \"...\", match = { class = \"...\" }, float = true })")
    local r = handle(t); state.window_rules[#state.window_rules + 1] = r; return r
  end,
  workspace_rule = function(t) local r = handle(t); state.workspace_rules[#state.workspace_rules + 1] = r; return r end,
  layer_rule = function(t) local r = handle(t); state.layer_rules[#state.layer_rules + 1] = r; return r end,
  curve = function(name, t) state.curves[name] = t end,
  animation = function(t) state.animations[#state.animations + 1] = t end,
  gesture = function(t) state.gestures[#state.gestures + 1] = t end,
  device = function(t) state.devices[#state.devices + 1] = t end,
  permission = function(path, kind, mode) state.permissions[#state.permissions + 1] = { path, kind, mode } end,
})

-- Helpers for lesson checks ----------------------------------------------------------------

local function norm_keys(keys)
  return (keys:gsub("%s+", ""):upper())
end

_hypr = state

function _hypr.find_bind(keys)
  local want = norm_keys(keys)
  for _, b in ipairs(state.binds) do
    if norm_keys(b.keys) == want then return b end
  end
end

function _hypr.start()
  if state.started then return end
  state.started = true
  state.execs_before_start = #state.execs
  for _, fn in ipairs(state.handlers["hyprland.start"] or {}) do fn() end
end

local function describe(action)
  local a = action.args
  if type(a) == "string" then return ("%s(%q)"):format(action.dispatcher, a) end
  if type(a) == "table" then
    local parts = {}
    for k, v in pairs(a) do parts[#parts + 1] = ("%s = %s"):format(k, tostring(v)) end
    table.sort(parts)
    return ("%s({ %s })"):format(action.dispatcher, table.concat(parts, ", "))
  end
  return action.dispatcher .. "()"
end

local function flatten(prefix, t, out)
  for k, v in pairs(t) do
    local key = prefix == "" and tostring(k) or (prefix .. "." .. tostring(k))
    if type(v) == "table" and not is_list(v) then flatten(key, v, out) else
      out[#out + 1] = ("%s = %s"):format(key, type(v) == "string" and ("%q"):format(v) or tostring(v))
    end
  end
  return out
end

-- Called by CodeQuest after your code runs.
function _cq_after()
  local lines = {}
  for _, line in ipairs(flatten("", state.config, {})) do lines[#lines + 1] = "  setting  " .. line end
  table.sort(lines)
  for _, m in ipairs(state.monitors) do lines[#lines + 1] = ("  monitor  %q %s at %s"):format(m.output or "", tostring(m.mode), tostring(m.position)) end
  for name, value in pairs(state.env) do lines[#lines + 1] = ("  env      %s=%s"):format(name, value) end
  for _, b in ipairs(state.binds) do
    local flags = {}
    for k, v in pairs(b.opts) do if v then flags[#flags + 1] = k end end
    table.sort(flags)
    lines[#lines + 1] = ("  bind     %-26s -> %s%s"):format(b.keys, describe(b.action),
      #flags > 0 and ("  [" .. table.concat(flags, ", ") .. "]") or "")
  end
  for event, fns in pairs(state.handlers) do lines[#lines + 1] = ("  on       %s (%d function%s)"):format(event, #fns, #fns == 1 and "" or "s") end
  for _, r in ipairs(state.window_rules) do lines[#lines + 1] = "  rule     window: " .. tostring(r.name or "(no name)") end
  if #lines == 0 then return end
  print("Hyprland would apply:")
  for _, line in ipairs(lines) do print(line) end
  local starts = state.handlers["hyprland.start"]
  if starts then
    local before = #state.execs
    _hypr.start()
    if #state.execs > before then
      print("At startup it would run:")
      for i = before + 1, #state.execs do print("  " .. state.execs[i]) end
    end
  end
end
