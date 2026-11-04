import math


def frames(signal, size, hop):
    return []


def dft_magnitudes(frame):
    return []


def hz_to_mel(f):
    return f


rate = 8000
tone = [math.sin(2 * math.pi * 1000 * n / rate) for n in range(64)]   # a 1000 Hz beep
fr = frames(tone, 16, 8)
print(len(fr), "frames of 16 samples")
mags = dft_magnitudes(fr[0]) if fr else []
print("magnitudes:", [round(m, 2) for m in mags])
if mags:
    peak = mags.index(max(mags))
    print("peak bin", peak, "=", peak * rate / 16, "Hz")
print("mel of 1000 Hz:", round(hz_to_mel(1000), 1))
