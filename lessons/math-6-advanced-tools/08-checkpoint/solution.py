import math
import statistics

T95 = {1: 12.706, 2: 4.303, 3: 3.182, 4: 2.776, 5: 2.571, 6: 2.447, 7: 2.365, 8: 2.306,
       9: 2.262, 10: 2.228, 11: 2.201, 12: 2.179, 13: 2.160, 14: 2.145, 15: 2.131,
       16: 2.120, 17: 2.110, 18: 2.101, 19: 2.093, 20: 2.086, 21: 2.080, 22: 2.074,
       23: 2.069, 24: 2.064, 25: 2.060, 26: 2.056, 27: 2.052, 28: 2.048, 29: 2.045, 30: 2.042}


def correlation(xs, ys):
    mx, my = statistics.mean(xs), statistics.mean(ys)
    cov = sum((x - mx) * (y - my) for x, y in zip(xs, ys)) / (len(xs) - 1)
    return cov / (statistics.stdev(xs) * statistics.stdev(ys))


def top_eigen(C, steps=200):
    v = [1.0] * len(C)
    for _ in range(steps):
        w = [sum(c * x for c, x in zip(row, v)) for row in C]
        n = math.sqrt(sum(x * x for x in w))
        v = [x / n for x in w]
    return sum(a * b for a, b in zip(v, [sum(c * x for c, x in zip(row, v)) for row in C]))


def welch(a, b):
    va, vb = statistics.variance(a) / len(a), statistics.variance(b) / len(b)
    t = (statistics.mean(a) - statistics.mean(b)) / math.sqrt(va + vb)
    df = (va + vb) ** 2 / (va ** 2 / (len(a) - 1) + vb ** 2 / (len(b) - 1))
    return t, df


def analyse(features, scores_a, scores_b):
    names = sorted(features)
    redundant = [(a, b) for i, a in enumerate(names) for b in names[i + 1:]
                 if abs(correlation(features[a], features[b])) > 0.95]
    Z = [[(x - statistics.mean(features[n])) / statistics.stdev(features[n]) for x in features[n]] for n in names]
    C = [[sum(a * b for a, b in zip(zi, zj)) / (len(zi) - 1) for zj in Z] for zi in Z]
    explained = top_eigen(C) / sum(C[i][i] for i in range(len(C)))
    t, df = welch(scores_a, scores_b)
    d = int(df)
    sig = abs(t) > (T95[d] if d <= 30 else 1.96)
    better = sig and statistics.mean(scores_a) > statistics.mean(scores_b)
    return {"redundant": redundant, "explained": explained, "t": t, "df": df, "better": better}


features = {
    "length_chars": [120, 340, 90, 560, 210, 430],
    "length_tokens": [31, 86, 24, 139, 54, 107],
    "rating": [4, 3, 5, 2, 4, 3],
}
A = [0.71, 0.74, 0.69, 0.73, 0.72, 0.70]
B = [0.68, 0.70, 0.69, 0.67, 0.71, 0.66]
print(analyse(features, A, B))
