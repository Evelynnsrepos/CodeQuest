// Runs TypeScript lessons in the browser, off the main thread. The real TypeScript compiler
// type-checks the learner's code (strict mode), then the compiled JavaScript runs here.
import ts from "/vendor/typescript.js";

const ready = (async () => {
  const res = await fetch("/vendor/typescript-lib.json");
  if (!res.ok) throw new Error("couldn't load the TypeScript library files");
  const files = await res.json();
  // Lessons only get what plain JavaScript has, plus console. No browser (DOM) APIs.
  files["lib.codequest.d.ts"] = `
    interface Console {
      log(...data: any[]): void; info(...data: any[]): void;
      warn(...data: any[]): void; error(...data: any[]): void;
    }
    declare var console: Console;`;
  const libs = new Map();
  for (const [name, text] of Object.entries(files)) {
    libs.set(name, ts.createSourceFile(name, text, ts.ScriptTarget.ES2022));
  }
  return libs;
})();

ready.then(() => self.postMessage({ type: "ready" }),
  (err) => self.postMessage({ type: "failed", error: String(err) }));

const OPTIONS = {
  strict: true,
  target: ts.ScriptTarget.ES2022,
  module: ts.ModuleKind.None,
  lib: ["lib.es2022.d.ts", "lib.codequest.d.ts"],
  types: [],
  noEmitOnError: true,
};

function compile(libs, code) {
  const main = ts.createSourceFile("main.ts", code, ts.ScriptTarget.ES2022);
  let js = "";
  const host = {
    getSourceFile: (name) => (name === "main.ts" ? main : libs.get(name.split("/").pop())),
    getDefaultLibFileName: () => "lib.es2022.d.ts",
    getDefaultLibLocation: () => "",
    writeFile: (name, text) => { if (name.endsWith(".js")) js = text; },
    getCurrentDirectory: () => "",
    getCanonicalFileName: (f) => f,
    useCaseSensitiveFileNames: () => true,
    getNewLine: () => "\n",
    fileExists: (f) => f === "main.ts" || libs.has(f.split("/").pop()),
    readFile: () => undefined,
    directoryExists: () => true,
    getDirectories: () => [],
  };
  const program = ts.createProgram(["main.ts"], OPTIONS, host);
  const problems = [...program.getSyntacticDiagnostics(main), ...program.getSemanticDiagnostics(main)];
  if (problems.length) return { problems: problems.map(describe).join("\n\n") };
  program.emit(main);
  return { js };
}

function describe(d) {
  const message = ts.flattenDiagnosticMessageText(d.messageText, "\n");
  if (!d.file) return message;
  const { line, character } = d.file.getLineAndCharacterOfPosition(d.start);
  return `main.ts:${line + 1}:${character + 1} - ${message}`;
}

// Print values roughly the way Node.js does, so console.log([1, 2]) shows [ 1, 2 ].
function show(value, depth = 0, nested = false) {
  if (typeof value === "string") return nested ? `'${value}'` : value;
  if (typeof value === "bigint") return `${value}n`;
  if (typeof value === "function") return `[Function: ${value.name || "(anonymous)"}]`;
  if (value === null || typeof value !== "object") return String(value);
  if (depth > 3) return Array.isArray(value) ? "[Array]" : "[Object]";
  const inner = (v) => show(v, depth + 1, true);
  const wrap = (open, parts, close) => (parts.length ? `${open} ${parts.join(", ")} ${close}` : `${open}${close}`);
  if (Array.isArray(value)) return wrap("[", value.map(inner), "]");
  if (value instanceof Map) return `Map(${value.size}) ` + wrap("{", [...value].map(([k, v]) => `${inner(k)} => ${inner(v)}`), "}");
  if (value instanceof Set) return `Set(${value.size}) ` + wrap("{", [...value].map(inner), "}");
  if (value instanceof Error) return value.stack || String(value);
  const name = value.constructor && value.constructor !== Object ? value.constructor.name + " " : "";
  const key = (k) => (/^[A-Za-z_$][\w$]*$/.test(k) ? k : `'${k}'`);
  return name + wrap("{", Object.entries(value).map(([k, v]) => `${key(k)}: ${inner(v)}`), "}");
}

const norm = (s) => s.trim().split("\n").map((l) => l.trimEnd()).join("\n");

function errorText(err) {
  return err instanceof Error ? `${err.name}: ${err.message}` : `Uncaught ${show(err, 0, true)}`;
}

self.onmessage = async (event) => {
  const { id, code, check, expected, mode } = event.data;
  const result = { output: "", error: null };
  try {
    const compiled = compile(await ready, code);
    if (compiled.problems) {
      result.error = "TypeScript found a problem before running your code:\n\n" + compiled.problems;
      if (mode === "submit") Object.assign(result, { passed: false, message: "Fix the type errors first." });
      return self.postMessage({ type: "result", id, result });
    }

    let out = "";
    const print = (...args) => { out += args.map((a) => show(a)).join(" ") + "\n"; };
    const sandboxConsole = { log: print, info: print, warn: print, error: print };
    // The check runs inside the same scope as the learner's code, so it can see their
    // top-level functions, classes and variables (const and let too).
    const body = `"use strict";\n${compiled.js}\n;return function (assert, output, code) {\n${check || ""}\n};`;
    let checker;
    try {
      checker = new Function("console", body)(sandboxConsole);
      await new Promise((r) => setTimeout(r, 0)); // let promise callbacks print
    } catch (err) {
      result.error = errorText(err);
    }
    result.output = out;
    if (mode === "submit") {
      result.passed = true;
      result.message = "";
      if (result.error) {
        Object.assign(result, { passed: false, message: "Your program stopped with an error." });
      } else if (expected != null && norm(out) !== norm(expected)) {
        Object.assign(result, { passed: false, message: "The output doesn't match yet.", expected: expected.trim() });
      } else if (check) {
        const assert = (ok, msg) => { if (!ok) throw new CheckFailed(msg); };
        try {
          checker(assert, out, code);
        } catch (err) {
          const message = err instanceof CheckFailed ? err.message || "Not quite yet."
            : "Your code raised an error while being checked:\n" + errorText(err);
          Object.assign(result, { passed: false, message });
        }
      }
    }
  } catch (err) {
    Object.assign(result, { error: String(err), passed: false });
  }
  self.postMessage({ type: "result", id, result });
};

class CheckFailed extends Error {}
