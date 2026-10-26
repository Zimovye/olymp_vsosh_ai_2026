y: list[int] = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0]
h1: list[int] = [1, 1, 1, 0, 0, 1, 1, 0, 0, 0, 1, 1]
h2: list[int] = [1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]

min_correct = 0
max_correct = 0
for i in range(len(y)):
    if h1[i] == h2[i]:
        if h1[i] == y[i]:
            min_correct += 1
            max_correct += 1
    else:
        max_correct += 1
print(max_correct)
print(min_correct)
