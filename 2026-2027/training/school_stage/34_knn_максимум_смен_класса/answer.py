from collections import Counter, defaultdict

# x, y, class
P = [
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
xs, ys = zip(*[(x, y) for x, y, _ in P])


# 1. Функция, которая принимает (X, Y) - координаты точки и просчитывает кол-во смен предсказаний класса [1; 18]
def calc(X, Y) -> int:
    # 1.1. Просчитываю расстояние от данной точки до каждой обучающей точки. Результат в переменную data: list[tuple[float, int]] - дистанция, класс
    data: list[tuple[float, int]] = []
    for x, y, c in P:
        dist = ((x - X) ** 2 + (y - Y) ** 2) ** 0.5
        data.append((dist, c))

    # 1.2. Сортирую переменную data в порядке возрастания дистанции до данной точки, при равным дистанциях по возрастанию класса
    sorted_data = sorted(data, key=lambda x: (x[0], x[1]))

    # 1.3 Создаю перменную clases_predicted, в котрую буду сохранять классы, которые предсказал
    #     и перменную current_t: int, в которую буду сохранять количество смен предсказанного класса
    clases_predicted: list[int] = []

    t = 0
    # 1.4. Цикл k от 1, до 18
    for k in range(1, len(P) + 1):
        # 1.4.1. В цикле прохожу по срезу data[k:]. Определяю класс данной точки, считая кол-во классов и сумму дистанций
        c_cnt = Counter()
        dist_cnt = defaultdict(float)

        for dist, c in sorted_data[:k]:
            c_cnt[c] += 1
            dist_cnt[c] += dist

        m = max(c_cnt.values())
        # Массив элементов с одинаковым количеством голосов за класс
        C = [c for c in c_cnt if c_cnt[c] == m]
        predicted_class = min(C, key=lambda x: (dist_cnt[x], x))

        # 1.4.2. Если предсказанный класс отличается от класса, который был предсказан до этого увеличиваем счётчик T
        if clases_predicted and predicted_class != clases_predicted[-1]:
            t += 1

        # 1.4.3. Записываю класс, который определил в перменную clases_predicted
        clases_predicted.append(predicted_class)

    # 1.5. Возвращаю количество изменений предсказанного класса для данной точки
    return t


# 2. Список содержащий: кол-во изменений, x, y для всех точек в прямоугольнике
Ts: list[tuple[int, int, int]] = []
for X in range(min(xs), max(xs) + 1):
    for Y in range(min(ys), max(ys) + 1):
        Ts.append((calc(X, Y), X, Y))

# 3. Находим максимальное значение
Tmax = max(Ts, key=lambda x: x[0])[0]
coords = [(x, y) for t, x, y in Ts if t == Tmax]
amount = len(coords)
coords = sorted(coords, key=lambda x: (x[0], x[1]))

print(Tmax)
print(amount)
for x, y in coords:
    print(x, y)
