from collections import Counter, defaultdict

train_points = [
    (7, 2, 1),
    (2, 10, 2),
    (8, 6, 3),
    (4, 1, 0),
    (9, 2, 1),
    (8, 0, 1),
    (9, 8, 3),
    (10, 8, 3),
    (7, 6, 3),
    (6, 1, 1),
    (0, 3, 0),
    (10, 4, 1),
    (5, 4, 0),
    (9, 0, 1),
    (2, 9, 2),
    (10, 2, 1),
    (0, 6, 2),
    (1, 9, 2),
    (1, 3, 0),
    (4, 3, 0),
]

validation_points = [
    (5, 5, 0),
    (9, 7, 3),
    (4, 4, 0),
    (6, 3, 1),
    (1, 2, 0),
    (6, 7, 3),
    (9, 10, 3),
    (0, 1, 0),
    (2, 5, 0),
    (4, 8, 2),
]

lambdas = [1, 4, 9, 16]
k = 5

# Первое, что приходит на ум это просто почистать для каждой лямбды одельно. Как лучше сделать?
# Может сделать словарь, или цикл for переместить в другое место или еще - я не знаю?
ans = {}
for lmbd in lambdas:
    cnt_correct = 0
    for X, Y, C in validation_points:
        data: list[tuple[float, int]] = []
        for x, y, c in train_points:
            dist = (x - X) ** 2 + lmbd * ((y - Y) ** 2)
            data.append((dist**0.5, c))
        sorted_data = sorted(data, key=lambda x: (x[0], x[1]))
        cnt_c = Counter()
        cnt_d = defaultdict(float)
        for d, c in sorted_data[:k]:
            cnt_c[c] += 1
            cnt_d[c] += d
        m = max(cnt_c.values())
        classes = [c for c in cnt_c if cnt_c[c] == m]
        pred_class = min(classes, key=lambda x: (cnt_d[x], x))

        if pred_class == C:
            cnt_correct += 1
    ans[lmbd] = cnt_correct

correct_counts = [ans[lmbd] for lmbd in lambdas]
max_correct = max(correct_counts)
best_lambdas = [lmbd for lmbd in lambdas if ans[lmbd] == max_correct]
print(" ".join(map(str, correct_counts)))
print(max_correct)
print(" ".join(map(str, best_lambdas)))
