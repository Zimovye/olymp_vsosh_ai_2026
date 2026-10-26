# Маленький готовый пример: вес координаты y меняет ближайших соседей.
train_points = [
    (-1, 2, 0),
    (1, 2, 0),
    (0, 3, 0),
    (-3, 0, 1),
    (3, 0, 1),
    (4, 0, 1),
]

validation_points = [(0, 0, 1)]
lambdas = [1, 4]
k = 3

correct_counts = []

for weight_y in lambdas:
    correct = 0

    for qx, qy, true_class in validation_points:
        distances = []

        for x, y, point_class in train_points:
            distance_squared = (qx - x) ** 2 + weight_y * (qy - y) ** 2
            distances.append((distance_squared, point_class))

        # Квадратный корень не нужен для порядка соседей:
        # меньше квадрат расстояния — меньше и само расстояние.
        distances.sort(key=lambda item: (item[0], item[1]))
        nearest = distances[:k]

        # Для каждого класса храним [число голосов, сумму расстояний].
        stats = {}
        for distance_squared, point_class in nearest:
            stats.setdefault(point_class, [0, 0])
            stats[point_class][0] += 1
            stats[point_class][1] += distance_squared**0.5

        predicted_class = min(
            stats,
            key=lambda point_class: (
                -stats[point_class][0],
                stats[point_class][1],
                point_class,
            ),
        )

        if predicted_class == true_class:
            correct += 1

        print("Вес y:", weight_y)
        print("Три соседа (квадрат расстояния, класс):", nearest)
        print("Предсказанный класс:", predicted_class)

    correct_counts.append(correct)

max_correct = max(correct_counts)
best_lambdas = []
for weight_y, correct in zip(lambdas, correct_counts):
    if correct == max_correct:
        best_lambdas.append(weight_y)

print("Число верных ответов:", correct_counts)
print("Лучшие веса:", best_lambdas)
