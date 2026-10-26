file = open("data.csv", encoding="utf-8")
file.readline()

data = []
for line in file:
    line = line.strip()
    x1, x2, y = list(map(int, line.split(",")))
    data.append((x1, x2, y))

file.close()

counts = 0
for x1, x2, y in data:
    s = 0.4 * x1 + 0.6 * x2
    is_allowed = y == 1 and s >= 5
    if is_allowed:
        counts += 1

print(counts)
