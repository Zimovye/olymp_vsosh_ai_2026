N = 500
accuracy = 0.4

correct = int(N * accuracy)
errors = N - correct

positive_counts = []
TP_counts = []
for TP in range(1, min(correct, errors) + 1):
    FP = TP
    TN = correct - TP
    FN = errors - FP

    postitive = TP + FN
    positive_counts.append(postitive)
    TP_counts.append(TP)

print(positive_counts)
print(min(TP_counts))
print(max(TP_counts))
