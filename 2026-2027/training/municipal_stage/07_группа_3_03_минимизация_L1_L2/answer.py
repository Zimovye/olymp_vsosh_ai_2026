from fractions import Fraction

y = [1, 2, 3, 9, 10, 10]
sorted_y = sorted(y)
n = len(y)

c1 = sorted_y[(n - 1) // 2]
c2 = Fraction(sum(y), n)

print(c1)
print(c2)
