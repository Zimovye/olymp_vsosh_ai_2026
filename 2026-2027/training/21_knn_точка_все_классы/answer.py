from collections import Counter, defaultdict

P = {
    0: [(8, 2), (8, 3), (9, 2)],
    1: [(3, 4), (4, 3), (5, 3), (2, 3)],
    2: [(7, 0), (8, -1), (7, -1), (6, 0), (5, 0)],
    3: [(1, 2), (6, 1), (4, 2), (2, 0), (2, 1), (4, 1)],
}
S = [(x, y, c) for c in P for x, y in P[c]]
xs, ys = zip(*[(x, y) for x, y, _ in S])


def seq(X, Y):
    # Посчитали расстояние от точки до всех других точек
    data = sorted([(((x - X) ** 2 + (y - Y) ** 2), c) for x, y, c in S])

    cnt = Counter()
    s = defaultdict(float)
    out = []
    for dist, point_class in data:
        cnt[point_class] += 1
        s[point_class] += dist**0.5
        m = max(cnt.values())

        C = [t for t in cnt if cnt[t] == m]
        out.append(min(C, key=lambda t: (s[t], t)))
    return out


answer = [
    (X, Y)
    for X in range(min(xs), max(xs) + 1)
    for Y in range(min(ys), max(ys) + 1)
    if len(set(seq(X, Y))) == 4
]
print(answer)
