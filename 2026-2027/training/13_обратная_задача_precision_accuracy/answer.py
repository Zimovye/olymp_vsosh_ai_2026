N = 1000
accuracy = 0.8
precision = 0.5

correct_answers = int(N * accuracy)
errors = N - correct_answers


positive_counts = []
TP_values = []
for TP in range(1, errors + 1):  # Почему errors, а не correct_answers?
    FP = TP
    TN = correct_answers - TP
    FN = errors - FP

    positive = TP + FN
    positive_counts.append(positive)

    TP_values.append(TP)

print(positive_counts)
print(min(TP_values))
print(max(TP_values))
