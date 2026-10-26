file = open("data.csv", encoding="utf-8")
file.readline()


def find_median(data: list[int | float]) -> float:
    sorted_data = sorted(data)
    n = len(data)
    middle = int(n / 2)

    if n % 2 == 0:
        mediana = (sorted_data[middle - 1] + sorted_data[middle]) / 2
    else:
        mediana = sorted_data[middle]

    return mediana


data = []
for line in file:
    x1, x2, y = map(int, line.strip().split(","))
    data.append((x1, x2, y))

file.close()

s_all: list[float] = []
for x1, x2, _ in data:
    s_all.append(0.4 * x1 + 0.6 * x2)

counts = 0
median = find_median(s_all)
for (x1, x2, y), s in zip(data, s_all):
    is_allowed = y == 1 and s >= median
    if is_allowed:
        counts += 1

print(counts)
