from fractions import Fraction

y = [3, 20, 5, 16, 7, 9]

print("c | L1 | L2")
for c in range(min(y), max(y) + 1):
    l1 = float("-inf")
    l2 = 0
    for x in y:
        l1_curr = abs(x - c)
        l1 = max(l1, l1_curr)
        l2 += (x - c) ** 2
    print(f"{c} | {l1} | {l2}")

# Всё равно не понимаю, почему для c1 - модуль, а для c2 - среднее.
# Да, я вижу по наглядной таблице, что это так, но почему так получается?
c1 = Fraction(min(y) + max(y), 2)
c2 = Fraction(sum(y), len(y))

print(c1)
print(c2)
