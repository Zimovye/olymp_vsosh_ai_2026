import numpy as np
import pandas as pd
from pathlib import Path
from collections import Counter

df = pd.read_csv(Path(__file__).with_name("watchtowers.csv"), encoding="utf-8")

# Башня без подходящих записей всё равно должна попасть в итоговый отчёт.
all_towers = sorted(set(df["tower_id"]))

df["timestamp"] = pd.to_datetime(df["timestamp"])

# Подготовка данных
good_hours = (df["rune_hours"] >= 1) & (df["rune_hours"] <= 96)

df = df[good_hours].copy()
mode_label = df["label"].mode().iloc[0]

df["label"] = df["label"].replace("", np.nan)

df["label"] = df["label"].fillna(mode_label)

rating_min = df["rating"].min()
rating_max = df["rating"].max()

df["rating_norm"] = (df["rating"] - rating_min) / (rating_max - rating_min)

# Оставляю только нужные
is_good = (
    (df["label"] == mode_label) & (df["rating_norm"] >= 0.8) & (df["rune_hours"] <= 48)
)

df = df[is_good].copy()

# Подчсёт визитов
print("После всех фильтров осталось записей:", len(df))

# В файле строки перемешаны. После сортировки каждая пара идёт по времени.
df = df.sort_values("timestamp")
last_time = {}
visits = Counter()

# zip берёт значения трёх столбцов одной строки, затем следующей строки.
for tower_id, creature, time in zip(df["tower_id"], df["creature"], df["timestamp"]):
    # Варг у другой башни и тролль у этой башни считаются отдельно.
    pair = (tower_id, creature)
    new_visit = pair not in last_time or time - last_time[pair] > pd.Timedelta(
        minutes=10
    )

    if new_visit:
        visits[pair] += 1
        print("Новый визит:", tower_id, creature, time)

    # Обновляем после КАЖДОЙ записи: нужен соседний снимок, а не начало визита.
    last_time[pair] = time


print("Итоговый отчёт:")
best_tower = all_towers[0]
best_total = -1

for tower_id in all_towers:
    # Counter возвращает 0, если такой пары не было среди новых визитов.
    wargs = visits[(tower_id, "варг")]
    trolls = visits[(tower_id, "тролль")]
    wyverns = visits[(tower_id, "виверна")]
    total = wargs + trolls + wyverns
    print(tower_id, wargs, trolls, wyverns, total)

    # Башни идут по возрастанию; при равенстве сохраняем уже найденную меньшую.
    if total > best_total:
        best_tower = tower_id
        best_total = total

print(best_tower, best_total)
