n = int(input())
p = [0] + list(map(int, input().split()))
d = map(int, input().split())
routs = [format(i, f"0{n}b") for i in range(2**n)]

path = {}
for number, idx in enumerate(d):
    code = routs[number]
    node = 1
    propability = 1

    for bit in code:
        if bit == "0":
            propability *= p[node]
            node = 2 * node
        else:
            propability *= 100 - p[node]
            node = 2 * node + 1
    path[idx] = path.get(idx, 0) + propability

path_unique = []
for idx, propability in path.items():
    path_unique.append((propability, idx))
path_unique.sort()

print(len(path))
for propability, idx in path_unique:
    print(idx, propability)
