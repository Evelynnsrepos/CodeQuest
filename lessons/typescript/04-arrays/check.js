assert(typeof totalGold === "function", "Write a function called totalGold.");
for (const [bags, want] of [[[5, 10, 20], 35], [[], 0], [[7], 7], [[1, 2, 3, 4], 10]]) {
  const got = totalGold(bags);
  assert(got === want, `totalGold(${JSON.stringify(bags)}) returned ${got}, expected ${want}.`);
}
assert(/bags\s*:\s*number\[\]/.test(code), "Keep the parameter type: bags: number[]");
