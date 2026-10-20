assert(typeof hpOf === "function", "Write a function called hpOf.");
const p = [{ name: "Ana", hp: 5 }, { name: "Bo", hp: 40 }];
assert(hpOf(p, "Bo") === 40, `hpOf(party, "Bo") should be 40, got ${hpOf(p, "Bo")}.`);
assert(hpOf(p, "Ana") === 5, `hpOf(party, "Ana") should be 5, got ${hpOf(p, "Ana")}.`);
assert(hpOf(p, "Zed") === 0, `hpOf(party, "Zed") should be 0 when nobody matches, got ${hpOf(p, "Zed")}.`);
assert(hpOf([], "Ana") === 0, "hpOf of an empty party should be 0.");
assert(!/hero!/.test(code), "Don't silence the error with hero!. Handle the undefined case instead.");
