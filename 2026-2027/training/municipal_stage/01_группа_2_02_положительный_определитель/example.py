from itertools import permutations


# Готовый учебный разбор исходной задачи: числа менять пока не нужно.
numbers = [1, 2, 3, 6]
all_variants = list(permutations(numbers))
good = 0

print("Всего расстановок:", len(all_variants))

for var in all_variants:
    # Читаем клетки по строкам: p, q сверху, r, s снизу.
    p = var[0]
    q = var[1]
    r = var[2]
    s = var[3]

    det = p * s - q * r
    print("Расстановка:", var, "ps =", p * s, "qr =", q * r,
          "Определитель:", det, "Подходит:", det > 0)

    # Ноль не подходит: по условию определитель должен быть строго положительным.
    if det > 0:
        good += 1

print("Подходящих расстановок:", good)
