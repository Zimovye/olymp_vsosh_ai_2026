file = open("data.csv", encoding="utf-8")
file.readline()

counts = 0
series_length = 0
for line in file:
    minute, anomaly = map(int, line.strip().split(","))
    if anomaly == 1:
        series_length += 1

        if series_length == 2:
            counts += 1
    else:
        series_length = 0

file.close()

print(counts)
