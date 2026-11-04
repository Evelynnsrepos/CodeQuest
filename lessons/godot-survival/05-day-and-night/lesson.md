---
title: Day and night
xp: 30
hint: Time moves by 24.0 / day_length * delta hours; fposmod(..., 24.0) wraps 24 back to 0.
hint: angle = time_of_day / 24.0 * TAU, day_amount = (1.0 - cos(angle)) / 2.0, then lerpf(night_brightness, 1.0, day_amount).
---
# The sun goes down

> **Warm-up:** How bright is it at midnight, at sunrise and at noon?

A survival day might last 10 real minutes. We keep the in-game clock as `time_of_day`, in hours from `0` to `24`, and move it forward every frame.

## Wrapping around midnight

After 23:59 comes 0:00, not 24:00. `fposmod(value, 24.0)` wraps a number into the range 0–24, like a clock:

```
fposmod(25.0, 24.0) = 1.0     (1 am the next day)
fposmod(23.5, 24.0) = 23.5    (unchanged)
fposmod(48.0, 24.0) = 0.0
```

("mod" is short for modulo: what's left over after taking away as many whole 24s as possible.)

## Hours per real second

If a full day (24 hours) lasts `day_length` real seconds, then each real second moves the clock forward by `24 / day_length` hours. With `day_length = 600` that's 0.04 hours (2.4 minutes) per second.

## Brightness that rises and falls smoothly

The light should be darkest at midnight (`0`), brightest at noon (`12`) and change gently in between. A **cosine** wave does exactly that. Let's build it in three steps.

**Step 1. Turn the hour into an angle.** One full day is one full turn: `angle = time_of_day / 24 × TAU`. Midnight is angle 0, noon is half a turn (`PI`).

**Step 2. Take the cosine.** You met cos in the shooter course: `cos(0) = 1` and `cos(PI) = -1`. In between it moves smoothly. So cos goes `1` at midnight, `-1` at noon, `1` again at the next midnight.

**Step 3. Flip and squeeze it to 0–1.** We want 0 at midnight and 1 at noon, the other way round, and without negative numbers:

```
day_amount = (1 - cos(angle)) / 2
```

Check midnight: (1 - 1) / 2 = 0 ✔. Check noon: (1 - (-1)) / 2 = 2 / 2 = 1 ✔. At 6 am, angle is a quarter turn, cos = 0, so (1 - 0) / 2 = 0.5, halfway ✔.

**Step 4. Blend.** Nights shouldn't be pitch black, so blend between `night_brightness` (0.2) and 1.0. `lerpf(a, b, t)` (*linear interpolation*) gives `a` when `t` is 0, `b` when `t` is 1, and the matching point in between otherwise:

```
lerpf(0.2, 1.0, 0)   = 0.2
lerpf(0.2, 1.0, 0.5) = 0.6     (halfway between 0.2 and 1.0)
lerpf(0.2, 1.0, 1)   = 1.0
```

The formula behind it is simple: `a + (b - a) × t`. For the middle one: 0.2 + 0.8 × 0.5 = 0.6.

In a 2D game you'd put this brightness into a `CanvasModulate` node's colour; in 3D into a `DirectionalLight3D`'s `light_energy`.

<svg viewBox="0 0 420 215" width="100%" style="max-width:420px" role="img" aria-label="Brightness over a day: lowest at midnight, rising smoothly to the brightest at noon and back, night shaded from 20:00 to 6:00"><defs><marker id="ahdn6c4cf5" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="#6c4cf5"/></marker><marker id="ahdne5484d" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="#e5484d"/></marker><marker id="ahdn30a46c" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="#30a46c"/></marker><marker id="ahdnd97706" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="#d97706"/></marker></defs><rect x="40.0" y="30.0" width="90.0" height="140.0" fill="#6c4cf5" opacity="0.12" rx="2"/><rect x="340.0" y="30.0" width="60.0" height="140.0" fill="#6c4cf5" opacity="0.12" rx="2"/><line x1="40.0" y1="170.0" x2="400.0" y2="170.0" stroke="currentColor" stroke-width="1.5" opacity="0.5"/><line x1="40.0" y1="30.0" x2="40.0" y2="170.0" stroke="currentColor" stroke-width="1.5" opacity="0.5"/><path d="M40.0,142.0 L43.8,141.9 L47.5,141.5 L51.2,140.9 L55.0,140.1 L58.8,139.0 L62.5,137.7 L66.2,136.2 L70.0,134.5 L73.8,132.6 L77.5,130.4 L81.2,128.1 L85.0,125.6 L88.8,122.9 L92.5,120.1 L96.2,117.1 L100.0,114.0 L103.8,110.8 L107.5,107.4 L111.2,104.0 L115.0,100.5 L118.8,96.9 L122.5,93.3 L126.2,89.7 L130.0,86.0 L133.8,82.3 L137.5,78.7 L141.2,75.1 L145.0,71.5 L148.8,68.0 L152.5,64.6 L156.2,61.2 L160.0,58.0 L163.8,54.9 L167.5,51.9 L171.2,49.1 L175.0,46.4 L178.8,43.9 L182.5,41.6 L186.2,39.4 L190.0,37.5 L193.8,35.8 L197.5,34.3 L201.2,33.0 L205.0,31.9 L208.8,31.1 L212.5,30.5 L216.2,30.1 L220.0,30.0 L223.8,30.1 L227.5,30.5 L231.2,31.1 L235.0,31.9 L238.8,33.0 L242.5,34.3 L246.2,35.8 L250.0,37.5 L253.8,39.4 L257.5,41.6 L261.2,43.9 L265.0,46.4 L268.8,49.1 L272.5,51.9 L276.2,54.9 L280.0,58.0 L283.8,61.2 L287.5,64.6 L291.2,68.0 L295.0,71.5 L298.8,75.1 L302.5,78.7 L306.2,82.3 L310.0,86.0 L313.8,89.7 L317.5,93.3 L321.2,96.9 L325.0,100.5 L328.8,104.0 L332.5,107.4 L336.2,110.8 L340.0,114.0 L343.8,117.1 L347.5,120.1 L351.2,122.9 L355.0,125.6 L358.8,128.1 L362.5,130.4 L366.2,132.6 L370.0,134.5 L373.8,136.2 L377.5,137.7 L381.2,139.0 L385.0,140.1 L388.8,140.9 L392.5,141.5 L396.2,141.9 L400.0,142.0" stroke="#d97706" stroke-width="2.5" fill="none"/><text x="40.0" y="186.0" font-size="11" fill="currentColor" text-anchor="middle">0:00</text><text x="130.0" y="186.0" font-size="11" fill="currentColor" text-anchor="middle">6:00</text><text x="220.0" y="186.0" font-size="11" fill="currentColor" text-anchor="middle">12:00</text><text x="310.0" y="186.0" font-size="11" fill="currentColor" text-anchor="middle">18:00</text><text x="400.0" y="186.0" font-size="11" fill="currentColor" text-anchor="middle">24:00</text><text x="34.0" y="34.0" font-size="11" fill="currentColor" text-anchor="end">1.0</text><text x="34.0" y="146.0" font-size="11" fill="currentColor" text-anchor="end">0.2</text><text x="85.0" y="44.0" font-size="11" fill="#6c4cf5" text-anchor="middle">night</text><text x="370.0" y="44.0" font-size="11" fill="#6c4cf5" text-anchor="middle">night</text><text x="220.0" y="24.0" font-size="11" fill="#d97706" text-anchor="middle">noon: brightest</text><text x="220.0" y="204.0" font-size="11" fill="currentColor" text-anchor="middle">brightness = lerp(0.2, 1.0, (1 − cos(angle)) ÷ 2)</text></svg>

## Your quest

1. `_process(delta)`: move `time_of_day` forward by `24.0 / day_length * delta` hours and wrap it with `fposmod`.
2. `brightness() -> float`: return the blended brightness from steps 1 to 4.
3. `is_night() -> bool`: `true` from 20:00 until 6:00 (20 or later, or before 6).

## Review

<details><summary>What does fposmod(25.0, 24.0) give?</summary>1.0: the clock wraps past midnight.</details>
<details><summary>What does lerpf(a, b, 0.5) give?</summary>The value halfway between a and b.</details>
<details><summary>Why use cos for brightness?</summary>It rises and falls smoothly in a loop, like the sun.</details>
