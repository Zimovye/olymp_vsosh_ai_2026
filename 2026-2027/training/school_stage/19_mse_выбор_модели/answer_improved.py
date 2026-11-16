teaching = [(-0.5, -0.75), (0, -0.5), (0.5, 1.25), (1, 1.5)]
verification = [(2, 5.0), (3, 11.5), (4, 14.0)]

models = [
    ("Model 1", lambda x: 2 * x),
    ("Model 2", lambda x: x + 0.5),
    ("Model 3", lambda x: (x + 2) ** 2 / 2 - 2),
    ("Model 4", lambda x: (x + 1) ** 2 - 1),
]


def find_best(points):
    results = []

    for name, model in models:
        errors = []

        for x, y in points:
            prediction = model(x)
            errors.append((y - prediction) ** 2)

        mse = sum(errors) / len(errors)
        print(name, "MSE =", mse)
        results.append({"name": name, "MSE": mse})

    best = min(results, key=lambda result: result["MSE"])
    return best["name"]


best_teaching = find_best(teaching)
print(f"Для обучающего набора лучшая модель: {best_teaching}")
best_all = find_best(teaching + verification)
print(f"Для точек из обоих наборов сразу лучшая модель: {best_all}")
