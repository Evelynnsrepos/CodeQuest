function count_potions(items)
    local count = 0
    for _, item in ipairs(items) do
        if item == "potion" then
            count = count + 1
        end
    end
    return count
end

print(count_potions({"potion", "sword", "potion"}))
