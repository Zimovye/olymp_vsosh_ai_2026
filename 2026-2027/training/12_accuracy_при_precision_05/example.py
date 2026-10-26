# Маленький учебный вариант: 20 объектов вместо 800.
N = 20
positive_objects = 5
negative_objects = N - positive_objects

accuracies = []

# При Precision = 0.5 верных и ошибочных положительных ответов поровну: TP = FP.
# TP начинается с 1, иначе у Precision получился бы нулевой знаменатель.
for TP in [1, 2, 3, 4, 5]:
    FP = TP
    FN = positive_objects - TP
    TN = negative_objects - FP

    precision = TP / (TP + FP)
    accuracy = (TP + TN) / N
    accuracies.append(accuracy)

    print("TP =", TP, "FP =", FP, "FN =", FN, "TN =", TN)
    print("Precision =", precision, "Accuracy =", accuracy)
    print()

print("Нижняя граница Accuracy:", min(accuracies))
print("Верхняя граница Accuracy:", max(accuracies))
