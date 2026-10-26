# Маленький учебный пример с двумя классами.
# В каждой строке: x, y, номер класса.
training_points = [
    (1, 0, 0),
    (0, 0, 1),
    (2, 0, 1),
    (3, 0, 1),
]


def get_predictions(query_x, query_y):
    neighbors = []

    for x, y, class_number in training_points:
        squared_distance = (x - query_x) ** 2 + (y - query_y) ** 2
        neighbors.append((squared_distance, class_number))

    # При равном расстоянии раньше идёт меньший номер класса.
    neighbors.sort()

    count_0 = 0
    count_1 = 0
    distance_sum_0 = 0
    distance_sum_1 = 0
    predictions = []

    # После добавления каждого соседа получаем ответ для нового значения k.
    for squared_distance, class_number in neighbors:
        distance = squared_distance ** 0.5

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
            if distance_sum_0 <= distance_sum_1:
                prediction = 0
            else:
                prediction = 1

        predictions.append(prediction)

    return predictions


answers = []

# В учебном наборе минимальный прямоугольник: x от 0 до 3, y = 0.
for query_x in range(0, 4):
    query_y = 0
    predictions = get_predictions(query_x, query_y)

    print("Точка:", (query_x, query_y))
    print("Классы при k = 1, 2, 3, 4:", predictions)
    print("Разные встречавшиеся классы:", set(predictions))
    print()

    if len(set(predictions)) == 2:
        answers.append((query_x, query_y))

print("Подходящие точки:", answers)
