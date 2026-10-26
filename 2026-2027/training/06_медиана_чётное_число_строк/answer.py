file = open("data.csv", encoding="utf-8")
file.readline()

data = []
assessments = []
for line in file:
    x1, x2, y = map(int, line.strip().split(","))
    s = 0.4 * x1 + 0.6 * x2
    assessments.append(s)
    data.append((s, y))

file.close()

n = len(assessments)
sorted_assessments = sorted(assessments)
middle = int(n / 2)
if n % 2 == 0:
    median = (sorted_assessments[middle - 1] + sorted_assessments[middle]) / 2
else:
    median = sorted_assessments[middle]

counts = 0
for s, y in data:
    if y == 1 and s >= median:
        counts += 1

print(counts)
