from itertools import permutations

variants = [1, 2, 3, 6]
all_vars = list(permutations(variants))

cnt = 0
for var in all_vars:
    p, q, r, s = var[0], var[1], var[2], var[3]
    det = p * s - q * r
    if det > 0:
        cnt += 1
print(cnt)
