file = open("data.csv", encoding="utf-8")
file.readline()

data = []
for line in file:
    p1_file, p2_file, y_file = line.strip().split(",")
    p1, p2 = float(p1_file), float(p2_file)
    y = int(y_file)

    q = 0.6 * p1 + 0.4 * p2
    data.append((q, y))

file.close()

counts = 0
for q, y in data:
    if q >= 0.6:
        prediction = 1
    else:
        prediction = 0

    if prediction != y:
        counts += 1

print(counts)
