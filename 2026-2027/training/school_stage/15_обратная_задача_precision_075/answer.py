N = 100
accuracy = 0.6

correct = int(N * accuracy)
errors = N - correct

positive_counts = []
TP_counts = []

for TP in range(3, min(correct, 3 * errors) + 1, 3):
    FP = TP // 3
    TN = correct - TP
    FN = errors - FP

    positive = TP + FN
    positive_counts.append(positive)
    TP_counts.append(TP)

print(f"P=[{min(positive_counts)};{max(positive_counts)}]")
print(f"TP=[{min(TP_counts)};{max(TP_counts)}]")
