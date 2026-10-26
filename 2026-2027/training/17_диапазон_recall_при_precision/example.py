# Маленький учебный вариант: 20 снимков вместо 1000.
N = 20
positive = 14
negative = N - positive

recalls = []

# Precision = 0.8 = 4/5, поэтому TP = 4 * FP.
# FP не может превышать число отрицательных снимков,
# а TP не может превышать число положительных снимков.
max_false_positive = min(negative, positive // 4)

for FP in range(1, max_false_positive + 1):
    TP = 4 * FP
    FN = positive - TP
    TN = negative - FP

    recall = TP / positive
    recalls.append(recall)

    print("TP =", TP, "FP =", FP, "FN =", FN, "TN =", TN)
    print("Recall =", round(recall, 3))
    print()

print("Нижняя граница Recall:", min(recalls))
print("Верхняя граница Recall:", max(recalls))
