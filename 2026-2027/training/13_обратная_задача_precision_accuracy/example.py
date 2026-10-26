# Маленький учебный вариант: 20 писем вместо 1000.
N = 20
accuracy = 0.75
precision = 0.5

correct_answers = int(N * accuracy)
errors = N - correct_answers

print("Всего верных ответов:", correct_answers)
print("Всего ошибок FP + FN:", errors)
print()

positive_counts = []
TP_values = []

# При Precision = 0.5 выполняется TP = FP.
# Все ошибки состоят из FP и FN, поэтому FN = errors - FP.
for TP in range(1, errors + 1):
    FP = TP
    FN = errors - FP
    TN = correct_answers - TP

    positive_letters = TP + FN

    positive_counts.append(positive_letters)
    TP_values.append(TP)

    print("TP =", TP, "FP =", FP, "FN =", FN, "TN =", TN)
    print("Число писем со спамом P =", positive_letters)
    print()

print("Возможные значения P:", positive_counts)
print("Нижняя граница TP:", min(TP_values))
print("Верхняя граница TP:", max(TP_values))
