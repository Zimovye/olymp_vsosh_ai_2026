p = [0] + list(map(int, input().split(" ")))
path = []

for number in range(8):
    code = format(number, "03b")
    node = 1
    propability = 1

    for bit in code:
        if bit == "0":
            propability *= p[node]
            node = 2 * node
        else:
            propability *= 100 - p[node]
            node = 2 * node + 1

    path.append((propability, code))

path.sort()

for _, code in path:
    print(code)
