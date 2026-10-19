local function media(key, cmd)
    hl.bind(key, hl.dsp.exec_cmd(cmd), { locked = true, repeating = true })
end

media("XF86AudioRaiseVolume", "wpctl set-volume -l 1 @DEFAULT_AUDIO_SINK@ 5%+")
media("XF86AudioLowerVolume", "wpctl set-volume @DEFAULT_AUDIO_SINK@ 5%-")
media("XF86AudioMute", "wpctl set-mute @DEFAULT_AUDIO_SINK@ toggle")
