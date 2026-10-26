N = 800
positive = 200
negative = N - positive

accuracies = []

for TP in range(3, positive + 1, 3):
    FP = TP // 3
    FN = positive - TP
    TN = negative - FP

    accuracy = (TP + TN) / N
    accuracies.append(accuracy)

print(min(accuracies))
print(max(accuracies))
