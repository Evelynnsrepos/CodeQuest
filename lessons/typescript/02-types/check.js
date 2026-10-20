assert(typeof level === "number" && level === 5, "level should be the number 5 (no quotes).");
assert(typeof heroName === "string", "heroName should be a string.");
assert(isAlive === true, "isAlive should be true.");
assert(/level\s*:\s*number/.test(code), "Keep the type annotation: let level: number = ...");
assert(output.trim() === "5", "Print level, which should show 5.");
