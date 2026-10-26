file = open("data.csv", encoding="utf-8")
file.readline()  # пропускаем заголовок x1,x2,y

rows = []
scores = []

for line in file:
    x1, x2, y = map(int, line.strip().split(","))

    score = 0.4 * x1 + 0.6 * x2
    rows.append((score, y))
    scores.append(score)

file.close()

# sorted() создаёт новую коллекцию и не меняет порядок значений в rows.
sorted_scores = sorted(scores)
n = len(sorted_scores)
middle = int(n / 2)

if n % 2 == 0:
    median = (sorted_scores[middle - 1] + sorted_scores[middle]) / 2
else:
    median = sorted_scores[middle]

print("Медиана:", round(median, 1))

allowed_count = 0

for score, y in rows:
    if y == 1 and score >= median:
        allowed_count += 1

print("Количество разрешённых участков:", allowed_count)
