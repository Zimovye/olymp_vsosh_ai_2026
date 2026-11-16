from fractions import Fraction

times = [2, 5, 8, 11, 14, 20]
counts = [3, 7, 2, 4, 3, 1]

print("c | L1 | L2")
for c in range(10):
    l1 = 0
    l2 = 0
    for t, k in zip(times, counts):
        l1 += k * abs(t - c)
        l2 += k * ((t - c) ** 2)
    print(f"{c} | {l1} | {l2}")

y = []
for t, k in zip(times, counts):
    for i in range(k):
        y.append(t)
n = len(y)

c1 = y[(n - 1) // 2]
c2 = Fraction(sum(y), n)

print(c1, c2)
