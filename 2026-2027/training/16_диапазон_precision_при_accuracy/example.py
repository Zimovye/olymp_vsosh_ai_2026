# Маленький учебный вариант: 20 объектов вместо 1000.
N = 20
positive = 8
negative = N - positive
accuracy = 0.75

correct = int(N * accuracy)
errors = N - correct

print("Всего верных ответов:", correct)
print("Всего ошибок:", errors)
print()

precisions = []

for TP in range(0, positive + 1):
    FN = positive - TP
    FP = errors - FN
    TN = correct - TP

    # Отрицательные количества объектов невозможны, а у Precision нужен знаменатель.
    if FP >= 0 and TN >= 0 and TP + FP > 0:
        precision = TP / (TP + FP)
        precisions.append(precision)

        print("TP =", TP, "FP =", FP, "FN =", FN, "TN =", TN)
        print("Precision =", round(precision, 3))
        print()

print("Нижняя граница Precision:", min(precisions))
print("Верхняя граница Precision:", max(precisions))
