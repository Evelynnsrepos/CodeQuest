assert(typeof describeReward === "function", "Write a function called describeReward.");
for (const [r, want] of [[50, "50 gold"], [1, "1 gold"], ["Fire Sword", "Item: Fire Sword"], ["Map", "Item: Map"]]) {
  const got = describeReward(r);
  assert(got === want, `describeReward(${JSON.stringify(r)}) returned ${JSON.stringify(got)}, expected ${JSON.stringify(want)}.`);
}
assert(/reward\s*:\s*(number\s*\|\s*string|string\s*\|\s*number)/.test(code), "Keep the union type: reward: number | string");
