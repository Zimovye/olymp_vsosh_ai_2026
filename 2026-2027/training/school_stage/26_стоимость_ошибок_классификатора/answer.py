N = 300
accuracy = 0.8

correct = int(accuracy * N)
errors = N - correct

output = []
for TP in range(1, errors + 1):  # Почему не correct?
    FP = TP
    FN = errors - FP

    C = 2 * FP + 5 * FN
    output.append((C, TP))

print(min(output, key=lambda x: x[0]))
print(max(output, key=lambda x: x[0]))
