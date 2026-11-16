from fractions import Fraction

N = 200
positive = 140
negative = N - positive

out = []
for FP in range(2, negative + 1, 2):
    TP = 3 * FP // 2
    FN = positive - TP
    TN = negative - FP

    if FN >= 0:
        F1 = Fraction(2 * TP, (2 * TP + FP + FN))
        out.append((F1, TP))

print(min(out, key=lambda x: x[0]))
print(max(out, key=lambda x: x[0]))
