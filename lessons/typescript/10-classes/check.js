assert(typeof Inventory === "function", "Write a class called Inventory.");
const inv = new Inventory();
for (const m of ["add", "has", "remove", "count"]) {
  assert(typeof inv[m] === "function", `Inventory needs a ${m} method.`);
}
assert(inv.count() === 0, "A new Inventory should have count() 0.");
inv.add("potion"); inv.add("potion"); inv.add("key");
assert(inv.count() === 3, `After adding 3 items count() should be 3, got ${inv.count()}.`);
assert(inv.has("key") === true && inv.has("map") === false, "has() should say whether an item is there.");
assert(inv.remove("potion") === true, "remove(\"potion\") should return true when it was there.");
assert(inv.count() === 2 && inv.has("potion"), "remove should take away only one copy.");
assert(inv.remove("map") === false, "remove(\"map\") should return false when it isn't there.");
assert(inv.count() === 2, "Removing a missing item shouldn't change the count.");
assert(/private\s+items/.test(code), "Keep items private.");
