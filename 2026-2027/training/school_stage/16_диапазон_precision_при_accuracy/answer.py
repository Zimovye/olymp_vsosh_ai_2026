N = 1000
accuracy = 0.8
positive = 400
negative = N - positive

correct = int(N * accuracy)
errors = N - correct

precision_counts = []
for TP in range(0, positive + 1):
    TN = correct - TP
    FP = negative - TN
    FN = errors - FP

    if FP >= 0 and FN >= 0 and TP + FP > 0:
        precision = TP / (TP + FP)
        precision_counts.append(precision)

print(min(precision_counts))
print(max(precision_counts))
