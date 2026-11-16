from fractions import Fraction

N = 180
accuracy = Fraction(5, 6)
correct = int(accuracy * N)
errors = N - correct

TP = 2 * errors
TN = correct - TP

possible = []
for FP in range(errors + 1):
    FN = errors - FP
    precision = Fraction(TP, TP + FP)
    possible.append((precision, FP))

print(TP)
print(TN)
print(len(possible))
print(min(possible, key=lambda x: x[0]))
print(max(possible, key=lambda x: x[0]))
