# Маленький учебный пример для целых x от -4 до 4.
# Здесь L(x) проще, чем в официальной задаче: L(x) = (x - 1)(x + 2).

x_min = -4
x_max = 4
suitable_x = []

for x in range(x_min, x_max + 1):
    L = (x - 1) * (x + 2)
    probability_cat = 1 / (1 + 2 ** (-L))
    probability_dog = 1 - probability_cat

    print(
        "x =", x,
        "L(x) =", L,
        "P(собачка) =", round(probability_dog, 3),
        "L(x) < 0:", L < 0,
    )

    # Порог 0.5 для собачки соответствует отрицательному значению L(x).
    if L < 0:
        suitable_x.append(x)

print("Подходящие целые x:", suitable_x)
print("Наибольшее подходящее x:", max(suitable_x))
