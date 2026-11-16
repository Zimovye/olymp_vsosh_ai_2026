from fractions import Fraction

y = [4, 17, 8, 13, 6, 11]


def penalty(c, y):
    """
    Вычисляет штраф за отклонение натяжения от идеального
    Args:
        c: текущее натяжение нити
        y: идеальное натяжение
    """
    if c < y:
        return 2 * (y - c)
    else:
        return c - y


print("c | F | L2")
for c in range(min(y), max(y) + 1):
    f = float("-inf")
    l2 = 0
    for x in y:
        f = max(f, penalty(c, x))
        l2 += (x - c) ** 2
    print(f"{c} | {f} | {l2}")

c1 = Fraction(16 + 11, 2)
c2 = Fraction(sum(y), len(y))

print(c1)
print(c2)
