from itertools import permutations

vars = [1, 2, 3, 4, 6, 7]
all_vars = list(permutations(vars, r=4))

cnt = 0
seen = set()
for var in all_vars:
    a, b, c, d = var[0], var[1], var[2], var[3]
    # Сортируем все четыре числа: состав не зависит от распределения по каналам.
    pair = tuple(sorted(var))
    if pair in seen:
        continue
    det = a * c - b * d
    if det >= 10 and det < 18:
        # Запоминаем комплект только после нахождения рабочей расстановки.
        seen.add(pair)
        cnt += 1
        print("Новый подходящий комплект:", pair, "Разность:", det, "Всего:", cnt)
print(cnt)
