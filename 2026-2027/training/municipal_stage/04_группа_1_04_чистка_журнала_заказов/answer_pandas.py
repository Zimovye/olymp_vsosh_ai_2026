import pandas as pd
import numpy as np
from pathlib import Path

df = pd.read_csv(Path(__file__).with_name("orders6_raw.csv"), encoding="utf-8")

good_hours = (df["delivery_hours"] >= 1) & (df["delivery_hours"] <= 96)
df = df[good_hours].copy()  # Зачем копировать таблицу?

df["label"] = df["label"].replace("", np.nan)
label_mode = df["label"].mode().iloc[0]
df["label"] = df["label"].fillna(label_mode)

min_rating = df["rating"].min()
max_rating = df["rating"].max()

df["rating_norm"] = (df["rating"] - min_rating) / (max_rating - min_rating)

is_good = (
    (df["label"] == label_mode)
    & (df["rating_norm"] >= 0.8)
    & (df["delivery_hours"] <= 48)
)
answer = is_good.sum()
print(answer)
