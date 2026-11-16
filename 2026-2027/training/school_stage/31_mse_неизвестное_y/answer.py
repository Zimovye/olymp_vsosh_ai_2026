n = 10
models = {1: lambda x: x + 1, 2: lambda x: 2 * x}

# 0 - 1 строго меньше 2, 1 - равны, 2 - 2 строго больше 1
answers = [[], [], []]
for y in range(0, n + 1):
    points = [(1, 2), (3, y)]
    MSEs = {}
    for number, model in models.items():
        squared_errors = []
        for X, Y in points:
            y_pred = model(X)
            squared_errors.append((Y - y_pred) ** 2)
        MSEs[number] = sum(squared_errors) / len(squared_errors)

    if MSEs[1] < MSEs[2]:
        answers[0].append(y)
    elif MSEs[1] == MSEs[2]:
        answers[1].append(y)
    else:
        answers[2].append(y)

for ans in answers:
    print(ans)
