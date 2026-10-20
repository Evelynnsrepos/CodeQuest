const alias = code.match(/type\s+Direction\s*=([^;\n]+)/);
assert(alias, "Write a type alias: type Direction = ...");
for (const d of ["up", "down", "left", "right"]) {
  assert(new RegExp(`["']${d}["']`).test(alias[1]), `Direction should include "${d}".`);
}
assert(!/\bstring\b/.test(alias[1]), "Direction should list the four exact values, not string.");
assert(typeof move === "function", "Write a function called move.");
const cases = [["up", 2, 2], ["down", 2, 4], ["left", 1, 3], ["right", 3, 3]];
for (const [d, x, y] of cases) {
  const from = { x: 2, y: 3 };
  const got = move(from, d);
  assert(got && got.x === x && got.y === y, `move({ x: 2, y: 3 }, "${d}") should give { x: ${x}, y: ${y} }, got ${JSON.stringify(got)}.`);
  assert(from.x === 2 && from.y === 3, "Return a new point instead of changing the one passed in.");
}
