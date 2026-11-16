from itertools import permutations

weights = [2, 3, 4, 6]
all_vars = list(permutations(weights))

cnt = 0
for var in all_vars:
    a, b, c, d = var[0], var[1], var[2], var[3]
    det = a * c - b * d
    if det >= 10 and det < 18:
        cnt += 1
print(cnt)
