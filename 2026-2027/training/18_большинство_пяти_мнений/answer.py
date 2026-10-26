file = open("data.csv", encoding="utf-8")
file.readline()

data = []
for line in file:
    y, n1, n2, n3, n4, n5 = map(int, line.strip().split(","))
    data.append((y, n1, n2, n3, n4, n5))

file.close()

counts = 0
for y, n1, n2, n3, n4, n5 in data:
    if n1 + n2 + n3 + n4 + n5 >= 3:
        prediction = 1
    else:
        prediction = 0
    is_correct = prediction == y
    if is_correct:
        counts += 1

print(counts)
