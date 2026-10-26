N = 800
positive = 200
negative = N - positive

accuracy_counts = []
for TP in range(1, min(positive, negative) + 1):
    FP = TP
    TN = negative - FP
    FN = positive - TP

    accuracy = (TP + TN) / N
    accuracy_counts.append(accuracy)

print(min(accuracy_counts))
print(max(accuracy_counts))
