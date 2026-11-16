from collections import Counter, defaultdict

S = [
    (8, 2, 1),
    (8, 3, 1),
    (9, 2, 1),
    (3, 4, 2),
    (4, 3, 2),
    (5, 3, 2),
    (2, 3, 2),
    (7, 0, 3),
    (8, -1, 3),
    (7, -1, 3),
    (6, 0, 3),
    (5, 0, 3),
    (1, 2, 4),
    (6, 1, 4),
    (4, 2, 4),
    (2, 0, 4),
    (2, 1, 4),
    (4, 1, 4),
]
xs, ys = zip(*[(x, y) for x, y, _ in S])


def seq(X, Y):
    data = sorted([(((x - X) ** 2 + (y - Y) ** 2), c) for x, y, c in S])

    cnt = Counter()
    s = defaultdict(float)
    output = []
    for d, c in data:
        cnt[c] += 1
        s[c] += d**0.5
        m = max(cnt.values())

        C = [t for t in cnt if cnt[t] == m]
        output.append(min(C, key=lambda t: (s[t], t)))
    return output


answer = [
    (X, Y)
    for X in range(min(xs), max(xs) + 1)
    for Y in range(min(ys), max(ys) + 1)
    if len(set(seq(X, Y))) == 4
]
