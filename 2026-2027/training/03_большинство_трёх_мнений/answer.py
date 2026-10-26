file = open("data.csv", encoding="utf-8")
file.readline()

data = []
for line in file:
    line = line.strip()
    n1_file, n2_file, n3_file, y_file = line.split(",")
    n1, n2, n3, y = int(n1_file), int(n2_file), int(n3_file), int(y_file)
    data.append((n1, n2, n3, y))

file.close()

counts = 0
for n1, n2, n3, y in data:
    if n1 + n2 + n3 >= 2:
        prediction = 1
    else:
        prediction = 0

    is_correct = prediction == y
    if is_correct:
        counts += 1

print(counts)
