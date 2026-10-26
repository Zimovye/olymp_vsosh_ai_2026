# x, y, class
training_points: list[tuple[int, int, int]] = [
    (8, 3, 0),
    (9, 2, 0),
    (4, 3, 1),
    (5, 3, 1),
    (2, 3, 1),
    (7, 0, 2),
    (8, -1, 2),
    (7, -1, 2),
    (6, 0, 2),
    (1, 2, 3),
    (6, 1, 3),
    (4, 2, 3),
    (2, 0, 3),
    (2, 1, 3),
    (4, 1, 3),
]

# x, y, class
points_to_check = [(8, 2, 0), (3, 4, 1), (5, 0, 2)]

# 1. Находим расстояния от проверяемой точки, до всех оставшихся точек
distances_points: dict[int, list[tuple[int, int]]] = {}
for x, y, point_class in training_points:
    for point_check_x, point_check_y, point_check_class in points_to_check:
        distance = ((x - point_check_x) ** 2 + (y - point_check_y) ** 2) ** 0.5
        distances_points.setdefault(point_check_class, []).append(
            (distance, point_class)
        )

# Сортируем
for _, distances in distances_points.items():
    distances.sort()

print(len(distances_points))

# 2. Определяем возможные `k`
possible_k = []
for k in range(1, len(distances) + 1):
    is_possible = True
    for point_check_class, distances in distances_points.items():
        selected_points = distances[:k]

        # 2.1 Считаем кол-во голосов
        class0 = {"CLASS": 0, "amount": 0, "distance": 0}
        class1 = {"CLASS": 1, "amount": 0, "distance": 0}
        class2 = {"CLASS": 2, "amount": 0, "distance": 0}
        class3 = {"CLASS": 3, "amount": 0, "distance": 0}
        for distance, point_class in selected_points:
            if point_class == 0:
                class0["amount"] += 1
                class0["distance"] += distance
            elif point_class == 1:
                class1["amount"] += 1
                class1["distance"] += distance
            elif point_class == 2:
                class2["amount"] += 1
                class2["distance"] += distance
            else:
                class3["amount"] += 1
                class3["distance"] += distance

        classes = [class0, class1, class2, class3]
        sorted_classes = sorted(
            classes, key=lambda x: (-x["amount"], x["distance"], x["CLASS"])
        )

        print(
            f'point_class ({point_check_class}) != sorted_classes[0]["CLASS"] ({sorted_classes[0]["CLASS"]})'
        )
        if point_check_class != sorted_classes[0]["CLASS"]:
            is_possible = False
            break

    if is_possible:
        possible_k.append(k)

print(possible_k)
