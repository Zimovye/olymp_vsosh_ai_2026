file = open("data.csv", encoding="utf-8")
file.readline()

col3 = []
for line in file:
    x = line.strip().split(",")[2]
    col3.append(int(x))

file.close()

avg = sum(col3) / len(col3)

counts = 0
for x in col3:
    if abs(x - avg) > avg:
        counts += 1

print(counts)
