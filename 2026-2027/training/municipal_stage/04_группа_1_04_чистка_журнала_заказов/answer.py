from collections import Counter
from pathlib import Path
from csv import reader

file = open(Path(__file__).with_name("orders6_raw.csv"), encoding="utf-8", newline="")
rows = reader(file)
next(rows)

orders = []
for delivery_hours, label, rating in rows:
    delivery_hours = float(delivery_hours)
    rating = float(rating)
    if 1 <= delivery_hours <= 96:
        orders.append([delivery_hours, label, rating])

# Нахожу моду label
labels = []
for _, label, _ in orders:
    if label != "":
        labels.append(label)
cnt_labels = Counter(labels)
mode_label = cnt_labels.most_common(1)[0][0]

# Заменяю пустые значения label её модой
for order in orders:
    if order[1] == "":
        order[1] = mode_label

# Нормализую rating
all_rating = [r[2] for r in orders]
min_rating, max_rating = min(all_rating), max(all_rating)

answer = 0
for delivery_hours, label, rating in orders:
    norm_rating = (rating - min_rating) / (max_rating - min_rating)
    is_good = label == mode_label and norm_rating >= 0.8 and delivery_hours <= 48
    if is_good:
        answer += 1
print(answer)
