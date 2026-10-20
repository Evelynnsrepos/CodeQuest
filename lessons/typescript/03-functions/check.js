assert(typeof damage === "function", "Write a function called damage.");
for (const [a, d, want] of [[10, 3, 7], [2, 8, 0], [5, 5, 0], [100, 1, 99]]) {
  const got = damage(a, d);
  assert(got === want, `damage(${a}, ${d}) returned ${got}, expected ${want}.`);
}
assert(/damage\s*[=(][^{]*:\s*number/.test(code), "Give damage a return type: (...): number");
