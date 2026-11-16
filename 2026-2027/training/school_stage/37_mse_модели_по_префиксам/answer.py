points: list[tuple[float, float]] = [
    (-0.5, -0.75),
    (0.0, -0.5),
    (0.5, 1.25),
    (1.0, 1.5),
    (2.0, 5.0),
    (3.0, 11.5),
    (4.0, 14.0),
]

models = [
    ("1", lambda x: 2 * x),
    ("2", lambda x: x + 0.5),
    ("3", lambda x: ((x + 2) ** 2) / 2 - 2),
    ("4", lambda x: (x + 1) ** 2 - 1),
]

# Перебираю все точки
b_all = []
change_prefixes = []  # как назвать переменную
errors: dict[str, list[float]] = {}  # Для каждой модели храним ошибки
for i, (x, y) in enumerate(points):
    MSEs: dict[str, float] = {}  # Для каждой модели храним MSE
    # Сначала определею MSE только 1-ой точки, потом 1-ой и 2-ой и тд.
    for name, model in models:
        y_pred = model(x)
        error = (y - y_pred) ** 2
        errors.setdefault(name, []).append(error)

        mse = sum(errors[name]) / len(errors[name])
        MSEs[name] = mse
    b = int(
        min(MSEs.items(), key=lambda x: (x[1], int(x[0])))[0]
    )  # Как бы лучше сделать?
    if b_all and b_all[-1] != b:
        change_prefixes.append(i + 1)
    b_all.append(b)

C = len(change_prefixes)
print(" ".join(map(str, b_all)))
print(C)
print(" ".join(map(str, change_prefixes)) if change_prefixes else -1)
