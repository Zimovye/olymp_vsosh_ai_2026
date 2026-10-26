models = [("1", lambda x: 2 * x), ("2", lambda x: x + 1)]
points = [(0, 2), (2, 2), (3, 4), (4, 9)]


def find_best(points: list[tuple[int, int]]) -> int:
    MSEs = []
    for number, model in models:
        errors = []
        for X, Y in points:
            y_pred = model(X)
            errors.append((Y - y_pred) ** 2)
        mse = sum(errors) / len(errors)
        MSEs.append((number, mse))
    if MSEs[0][1] < MSEs[1][1]:
        return 1
    elif MSEs[0][1] == MSEs[1][1]:
        return 0
    else:
        return 2


results = [find_best(points)]
changed_points = []  # не знал как назвать переменную лучше
for point_to_delete in [0, 1, 2, 3]:
    data = points.copy()
    data.pop(point_to_delete)

    result = find_best(data)
    results.append(result)
    if result != results[0]:
        changed_points.append(point_to_delete + 1)

print(" ".join(map(str, results)))
print(" ".join(map(str, changed_points)) if changed_points else -1)
