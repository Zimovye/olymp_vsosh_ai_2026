N = 200
positive = 120
negative = N - positive

for TP in range(3, positive + 1, 3):
    FP = TP // 3
    recall = TP / positive

    if recall >= 0.8:
        FN = positive - TP
        TN = negative - FP

        print(TP + FP)
        print(TP)
        print(FP)
        print(FN)
        print(TN)
        break
