from fractions import Fraction

values = [2, 5, 8, 11, 14, 20]
counts = [3, 7, 2, 4, 3, 1]
settings = [12, 7, 3, 9, 6, 18]

# y = sorted([v for v, c in zip(values, counts) for _ in range(c)])

min_l1 = float("inf")
min_c1 = 0
min_l2 = float("inf")
min_c2 = 0
for c in sorted(settings):
    l1 = 0
    l2 = 0
    for x, k in zip(values, counts):
        l1 += k * abs(x - c)
        l2 += k * ((x - c) ** 2)
    if l1 < min_l1:
        min_l1 = l1
        min_c1 = c
    if l2 < min_l2:
        min_l2 = l2
        min_c2 = c

print(min_c1)
print(min_c2)
