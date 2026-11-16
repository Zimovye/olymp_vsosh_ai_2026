from csv import reader
from collections import Counter
from pathlib import Path


# 1. Читаем настоящий CSV. Файл ищем рядом с этой программой.
file = open(Path(__file__).with_name("orders_train.csv"), encoding="utf-8", newline="")
rows = reader(file)
next(rows)  # Заголовок содержит названия столбцов, а не данные заказа.

orders = []
for hours, label, rating in rows:
    hours = float(hours)
    rating = float(rating)
    # Удалённые заказы не должны влиять на моду и границы рейтингов.
    if 1 <= hours <= 96:
        orders.append([hours, label, rating])
file.close()
print("После фильтрации осталось заказов:", len(orders))


# 2. Пустая метка не участвует в выборе самой частой метки.
labels = []
for hours, label, rating in orders:
    if label != "":
        labels.append(label)

label_counts = Counter(labels)
print("Частоты непустых меток:", label_counts)
# most_common(1) вернёт [('обычный', 5)]; нам нужно только слово.
mode_label = label_counts.most_common(1)[0][0]
print("Мода:", mode_label)

for order in orders:
    if order[1] == "":
        order[1] = mode_label


# 3. Границы берём по всем оставшимся заказам, включая доставку дольше 48 часов.
ratings = []
for hours, label, rating in orders:
    ratings.append(rating)

rating_min = min(ratings)
rating_max = max(ratings)
print("Минимальный рейтинг:", rating_min)
print("Максимальный рейтинг:", rating_max)


# 4. Теперь проверяем три условия одновременно.
answer = 0
for hours, label, rating in orders:
    rating_norm = (rating - rating_min) / (rating_max - rating_min)
    good = label == mode_label and rating_norm >= 0.8 and hours <= 48
    # Округляем только показ: решение уже принято по неокруглённому значению.
    print(hours, label, rating, "нормированный:", round(rating_norm, 2), "подходит:", good)
    if good:
        answer += 1

print("Ответ для учебного файла:", answer)
