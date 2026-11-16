N = 1000
positive = 850
negative = N - positive

recalls = []
for TP in range(4, min(positive, negative * 4) + 1, 4):
    FP = TP // 4
    TN = negative - FP
    FN = positive - TP

    recall = TP / positive
    recalls.append(recall)

print(min(recalls))
print(max(recalls))
