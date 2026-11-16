import numpy as np
import pandas as pd
from pathlib import Path
from collections import Counter

df = pd.read_csv(Path(__file__).with_name("watchtowers.csv"), encoding="utf-8")
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
df = df.sort_values("timestamp")
last_time = {}
visits = Counter()

for tower_id, creature, time in zip(df["tower_id"], df["creature"], df["timestamp"]):
    pair = (tower_id, creature)
    new_visit = pair not in last_time or time - last_time[pair] > pd.Timedelta(
        minutes=10
    )

    if new_visit:
        visits[pair] += 1

    last_time[pair] = time


best_tower = all_towers[0]
best_vivists = -1

for tower_id in all_towers:
    wargs = visits[(tower_id, "варг")]
    troll = visits[(tower_id, "тролль")]
    wyverns = visits[(tower_id, "виверна")]
    total = wargs + troll + wyverns

    print(tower_id, wargs, troll, wyverns, total)

    if total > best_vivists:
        best_tower = tower_id
        best_vivists = total

print(best_tower, best_vivists)
