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

# Уравниваем крайние штрафы: c - min(y) = 2 * (max(y) - c).
c1 = Fraction(min(y) + 2 * max(y), 3)
c2 = Fraction(sum(y), len(y))

print("Крайние идеальные значения:", min(y), max(y))
print("Штраф для минимального при c1:", penalty(c1, min(y)))
print("Штраф для максимального при c1:", penalty(c1, max(y)))
print("Ответы:")
print(c1)
print(c2)
