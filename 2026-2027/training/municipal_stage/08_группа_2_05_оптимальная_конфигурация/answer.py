k = int(input())

for gen in range(1, 9):
    update = gen * k
    total = gen + update
    if total % 8 == 0:
        nodes = total // 8
        break
print(nodes)
