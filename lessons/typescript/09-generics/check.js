assert(typeof firstOr === "function", "Write a function called firstOr.");
assert(firstOr([3, 9], 0) === 3, `firstOr([3, 9], 0) should be 3, got ${firstOr([3, 9], 0)}.`);
assert(firstOr([], "none") === "none", "firstOr([], \"none\") should be \"none\".");
assert(firstOr(["sword"], "fists") === "sword", "firstOr([\"sword\"], \"fists\") should be \"sword\".");
assert(firstOr([0, 5], 9) === 0, "firstOr([0, 5], 9) should be 0. Check the length, not whether the first item is truthy.");
assert(firstOr([undefined, 1], 7) === undefined, "If the array has items, return the first one even if it's undefined.");
assert(/firstOr\s*<\s*T\s*>/.test(code), "Make it generic: function firstOr<T>(...)");
