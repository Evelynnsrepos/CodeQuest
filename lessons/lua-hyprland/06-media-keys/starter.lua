local function media(key, cmd)
    -- Bind key to run cmd, with locked and repeating turned on
end

media("XF86AudioRaiseVolume", "wpctl set-volume -l 1 @DEFAULT_AUDIO_SINK@ 5%+")
-- Add the other two keys
