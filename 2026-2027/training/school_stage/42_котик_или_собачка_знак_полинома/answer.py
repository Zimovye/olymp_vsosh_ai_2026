x = 1
suitable_x = []
while True:
    L = (x - 1) ** 2 * (x + 1) * (x + 2) * (2 * x + 1)
    cat = 1 / (1 + 2 ** (-L))
    dog = 1 - cat

    if dog > 0.5:
        suitable_x.append(x)

    if L < 0:
        break

    x -= 1

print(max(suitable_x))
