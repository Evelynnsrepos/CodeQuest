assert(type(coins_for) == "function", "Write a function called coins_for.")
for _, case in ipairs({ {1, 50}, {4, 200}, {0, 0}, {10, 500} }) do
  local got = coins_for(case[1])
  assert(got == case[2], ("coins_for(%d) returned %s, expected %d."):format(case[1], tostring(got), case[2]))
end
