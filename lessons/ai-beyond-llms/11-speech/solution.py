import math


def frames(signal, size, hop):
    out = []
    for start in range(0, len(signal) - size + 1, hop):
        out.append(signal[start:start + size])
    return out


def dft_magnitudes(frame):
    N = len(frame)
    mags = []
    for k in range(N // 2 + 1):
        re = 0
        im = 0
        for n in range(N):
            angle = 2 * math.pi * k * n / N
            re = re + frame[n] * math.cos(angle)
            im = im - frame[n] * math.sin(angle)
        mags.append(math.sqrt(re * re + im * im))
    return mags


def hz_to_mel(f):
    return 2595 * math.log10(1 + f / 700)


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
