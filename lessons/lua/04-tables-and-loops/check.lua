assert(type(count_potions) == "function", "Write a function called count_potions.")
local cases = {
  { {"potion", "sword", "potion"}, 2 },
  { {}, 0 },
  { {"sword", "shield"}, 0 },
  { {"potion", "potion", "potion", "potion"}, 4 },
}
for _, case in ipairs(cases) do
  local got = count_potions(case[1])
  assert(got == case[2], ("count_potions({%s}) returned %s, expected %d."):format(
    table.concat(case[1], ", "), tostring(got), case[2]))
end
