file = open("data.csv", encoding="utf-8")
file.readline()

counts = 0
series_length = 0
for line in file:
    failure = int(line.strip().split(",")[1])

    if failure == 1:
        series_length += 1
        counts = max(counts, series_length)
    else:
        series_length = 0

file.close()

print(counts)
