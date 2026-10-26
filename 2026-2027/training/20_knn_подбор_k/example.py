# Маленький учебный пример: одна проверяемая точка и два класса.
query_x = 0
query_y = 0
true_class = 0

# В каждой строке: x, y, номер класса.
training_points = [
    (1, 0, 0),
    (0, 2, 1),
    (3, 0, 0),
    (0, 4, 1),
    (5, 0, 1),
]

neighbors = []

for x, y, class_number in training_points:
    distance = ((x - query_x) ** 2 + (y - query_y) ** 2) ** 0.5
    neighbors.append((distance, class_number, x, y))

# Кортежи сортируются сначала по расстоянию, затем по номеру класса.
neighbors.sort()

print("Соседи от ближайшего к дальнему:")
for distance, class_number, x, y in neighbors:
    print((x, y), "класс", class_number, "расстояние", round(distance, 3))

print()

for k in range(1, len(neighbors) + 1):
    selected_neighbors = neighbors[:k]

    count_0 = 0
    count_1 = 0
    distance_sum_0 = 0
    distance_sum_1 = 0

    for distance, class_number, x, y in selected_neighbors:
        if class_number == 0:
            count_0 += 1
            distance_sum_0 += distance
        else:
            count_1 += 1
            distance_sum_1 += distance

    if count_0 > count_1:
        prediction = 0
    elif count_1 > count_0:
        prediction = 1
    else:
        # При равных голосах побеждает меньшая сумма расстояний.
        # Если равны и суммы, класс 0 имеет меньший номер.
        if distance_sum_0 <= distance_sum_1:
            prediction = 0
        else:
            prediction = 1

    print("k =", k)
    print("Голоса классов 0 и 1:", count_0, count_1)
    print("Суммы расстояний:", round(distance_sum_0, 3),
          round(distance_sum_1, 3))
    print("Предсказанный класс:", prediction)
    print("Правильно:", prediction == true_class)
    print()
