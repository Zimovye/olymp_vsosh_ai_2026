# Маленький готовый пример: 4 задания и не более 10 единиц времени.
# Действия: 0 — списать, 1 — решить с подсказкой, 2 — самостоятельно.

n = 4
time_limit = 10

best_score_numerator = -1
best_strategy = []

for number in range(3**n):
    strategy = []

    # Получаем n троичных цифр. В отличие от прошлого задания,
    # основание равно 3, потому что на каждой позиции три действия.
    for position in range(n - 1, -1, -1):
        action = (number // (3**position)) % 3
        strategy.append(action)

    K = 0
    sum_h = 0
    time_spent = 0

    for action in strategy:
        if action == 0:
            H = 4.5
            time_spent += 1
        elif action == 1:
            H = min(3 + 0.5 * K, 5)
            K += 0.5
            time_spent += 2
        else:
            H = min(1.5 + 0.25 * K, 5)
            K += 1
            time_spent += 4

        sum_h += H

    if time_spent > time_limit:
        continue

    E = min(1 + 0.5 * K, 5)

    # S = (4 * sum(H) + 6 * n * E) / (10 * n).
    # Для сравнения достаточно числителя: знаменатель у всех один.
    score_numerator = 4 * sum_h + 6 * n * E

    if score_numerator > best_score_numerator:
        best_score_numerator = score_numerator
        best_strategy = strategy

        S = score_numerator / (10 * n)
        print("Новый лучший вариант:", "".join(map(str, strategy)))
        print("Время:", time_spent, "Знания:", K, "Итог:", S)

S_max = best_score_numerator / (10 * n)
print("Лучшая стратегия:", "".join(map(str, best_strategy)))
print("Максимальный итог:", S_max)
