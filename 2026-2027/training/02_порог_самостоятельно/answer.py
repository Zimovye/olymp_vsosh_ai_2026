file = open("data.csv", encoding="utf-8")

file.readline()

data = []
for line in file:
    line = line.strip()
    p_line, y_line = line.split(",")

    p = float(p_line)
    y = int(y_line)

    data.append((p, y))

file.close()

counts = 0
for p, y in data:
    if p >= 0.65:
        prediction = 1
    else:
        prediction = 0

    is_correct = prediction == y

    if is_correct:
        counts += 1

print(counts)
