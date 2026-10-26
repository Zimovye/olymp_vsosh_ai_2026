file = open("data.csv", encoding="utf-8")
file.readline()

max_length = 0
series_length = 0

for line in file:
    failure = int(line.strip().split(",")[1])

    if failure == 1:
        series_length += 1
        max_length = max(max_length, series_length)
    else:
        series_length = 0

file.close()

print(max_length)
