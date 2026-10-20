assert(/interface\s+Hero\b/.test(code), "Write an interface called Hero.");
assert(typeof levelUp === "function", "Write a function called levelUp.");
const before = { name: "Mo", hp: 20, level: 3 };
const after = levelUp(before);
assert(after && after.level === 4, `levelUp should raise level 3 to 4, got ${after && after.level}.`);
assert(after.hp === 30, `levelUp should raise hp 20 to 30, got ${after.hp}.`);
assert(after.name === "Mo", "Keep the hero's name.");
assert(after !== before && before.level === 3 && before.hp === 20,
  "Return a new object and leave the original hero unchanged. Try { ...hero, ... }.");
assert(/levelUp\s*\(\s*hero\s*:\s*Hero\s*\)\s*:\s*Hero/.test(code), "Use the types: levelUp(hero: Hero): Hero");
