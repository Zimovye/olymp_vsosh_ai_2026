from pathlib import Path
import numpy as np
import pandas as pd
from collections import Counter

df = pd.read_csv(Path(__file__).with_name("forges.csv"), encoding="utf-8")

df["timestamp"] = pd.to_datetime(df["timestamp"])
all_forges = sorted(set(df["forge_id"]))

good_hours = (df["rune_hours"] >= 1) & (df["rune_hours"] <= 96)
df = df[good_hours].copy()

df["label"] = df["label"].replace("", np.nan)
mode_label = df["label"].mode().iloc[0]
df["label"] = df["label"].fillna(mode_label)

rating_min = df["rating"].min()
rating_max = df["rating"].max()

df["rating_norm"] = (df["rating"] - rating_min) / (rating_max - rating_min)
good = (
    (df["rating_norm"] >= 0.8) & (df["label"] == mode_label) & (df["rune_hours"] <= 48)
)
df = df[good].copy()

df = df.sort_values("timestamp")

visits = Counter()
last_visit = {}
durations = {}
for forge_id in all_forges:
    durations[forge_id] = pd.Timedelta(minutes=0)

for forge_id, craft, time in zip(df["forge_id"], df["craft"], df["timestamp"]):
    pair = (forge_id, craft)
    new_visit = pair not in visits or time - last_visit[pair] > pd.Timedelta(minutes=10)

    if new_visit:
        visits[pair] += 1
    else:
        gap = time - last_visit[pair]
        durations[forge_id] += gap
    last_visit[pair] = time

best_forge = all_forges[0]
best_minutes = -1

for forge_id in all_forges:
    swords = visits[(forge_id, "меч")]
    shields = visits[(forge_id, "щит")]
    armor = visits[(forge_id, "латы")]
    total = swords + shields + armor

    minutes = int(durations[forge_id] / pd.Timedelta(minutes=1))

    if minutes > best_minutes:
        best_forge = forge_id
        best_minutes = minutes

    print(forge_id, swords, shields, armor, total, minutes)

print(best_forge, best_minutes)
