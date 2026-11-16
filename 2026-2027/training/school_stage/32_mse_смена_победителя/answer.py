points = [(0, 0), (1, 2)]
n = 3
points_to_append = [(2, 4), (3, 4), (4, 8)]
models = [("1", lambda x: x * 2), ("2", lambda x: x + 1)]


def find_best() -> str:
    MSEs = []
    for name, model in models:
        errors = []
        for X, Y in points:
            y_pred = model(X)
            errors.append((Y - y_pred) ** 2)
        mse = sum(errors) / len(errors)
        MSEs.append({"name": name, "MSE": mse})

    if MSEs[0]["MSE"] == MSEs[1]["MSE"]:
        return "0"

    best = min(MSEs, key=lambda x: x["MSE"])
    return best["name"]


result = [find_best()]
result_number = -1
for addition_number in range(1, len(points_to_append) + 1):
    points.append(points_to_append[addition_number - 1])
    current = find_best()
    if result_number == -1 and current != result[-1]:
        result_number = addition_number
    result.append(current)

print(" ".join(result))
print(result_number)
