from collections import Counter, defaultdict

points = [
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

# Словарь ks = {номер k, счётчик кол-ва верно предсказанных точек}
ks = Counter()


# Функция определения класса для точки для каждого k будет проверять C == predicted_c и добавлять в `ks`
def define_class(X, Y, C):
    data: list[tuple[float, int]] = []  # дистанция до точки, класс точки
    # Переберяю все точки в массиве points и определяю расстояние для кажой точки
    for x, y, c in points:
        dist = ((x - X) ** 2 + (y - Y) ** 2) ** 0.5
        data.append((dist, c))

    # Перебор всех `k`
    for k in range(1, len(points) + 1):
        # Сортирую data по (возрастанию дистанции, возрастанию класса)
        sorted_data = sorted(data, key=lambda x: (x[0], x[1]))

        # Беру k ближайших точек, считаю голоса за класс и сумму растояний
        c_cnt = Counter()
        d_cnt = defaultdict(float)
        for d, c in sorted_data[:k]:
            c_cnt[c] += 1
            d_cnt[c] += d
        m = max(c_cnt.values())
        classes = [c for c in c_cnt if c_cnt[c] == m]
        predicted_class = min(classes, key=lambda c: (d_cnt[c], c))

        # Проверяю правильно ли определён класс для точки с текущим k
        if predicted_class == C:
            ks[k] += 1


# Перебор всех точек i (запоминаю индекс, удаляю pop() и с помощью .insert() вставляю обратно)
for i, (x, y, c) in enumerate(points):
    point = points.pop(i)
    define_class(point[0], point[1], point[2])
    points.insert(i, point)

Amax = max(ks)
answer = sorted(k for k, v in ks.items() if v == Amax)
print(Amax)
print(" ".join(map(str, answer)))
