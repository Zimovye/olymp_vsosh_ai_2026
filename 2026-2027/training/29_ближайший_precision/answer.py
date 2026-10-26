from fractions import Fraction

N = 180
accuracy = 0.8

positive = 70
negative = N - positive
correct = int(N * accuracy)
errors = N - correct

out = []
for TP in range(0, positive + 1):
    TN = correct - TP
    FP = negative - TN
    FN = errors - FP
    if TN >= 0 and FP >= 0:
        precision = Fraction(TP, (TP + FP))
        D = abs(precision - Fraction(18, 25))
        out.append((D, precision, TP, FP, FN, TN))

best = min(out, key=lambda x: x[0])
print(best[2], best[3], best[4], best[5])
print(best[1])
print(best[0])
