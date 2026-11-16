N = 200
accuracy = 0.8

correct = int(N * accuracy)
errors = N - correct

out = []
for TP in range(2, errors + 1, 2):
    FP = 3 * TP // 2
    FN = errors - FP
    TN = correct - TP
    if FN >= 0:
        positive = TP + FN
        out.append((positive, TP))

print(len(out))
print(min(out, key=lambda x: x[0]))
print(max(out, key=lambda x: x[0]))
