p = [0] + list(map(int, input().split()))
d = map(int, input().split())
path = {}

routes = [format(i, "03b") for i in range(8)]

for number, idx in enumerate(d):
    code = routes[number]
    node = 1
    propabitity = 1

    for bit in code:
        if bit == "0":
            propabitity *= p[node]
            node = 2 * node
        else:
            propabitity *= 100 - p[node]
            node = 2 * node + 1

    path[idx] = path.get(idx, 0) + propabitity

path_unique = []
for idx, prob in path.items():
    path_unique.append((prob, idx))

path_unique.sort()

print(len(path))
for propabitity, idx in path_unique:
    print(idx, propabitity)
