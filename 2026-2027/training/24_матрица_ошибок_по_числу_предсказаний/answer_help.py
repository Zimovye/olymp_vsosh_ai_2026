from fractions import Fraction


N = 120

positive = 50
negative = N - positive
accuracy = 0.75

correct = int(accuracy * N)
errors = N - correct

predicted_positive = 60

for TP in range(0, positive + 1):
    FP = predicted_positive - TP
    FN = positive - TP
    TN = negative - FP

    # Подходит только четвёрка с нужным числом верных ответов и ошибок.
    if FP >= 0 and FN >= 0 and TN >= 0 and TP + TN == correct and FP + FN == errors:
        precision = Fraction(TP, TP + FP)

        print("TP =", TP)
        print("FP =", FP)
        print("FN =", FN)
        print("TN =", TN)
        print("Precision =", precision)
