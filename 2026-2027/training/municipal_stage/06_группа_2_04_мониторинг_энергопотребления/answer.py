import pandas as pd

df = pd.read_csv("ts6_raw.csv", encoding="utf-8")

df["diff_1"] = df["power"].diff()
# Что такое min_periods=8?
df["ma_8"] = df["power"].rolling(window=8, min_periods=8).mean()
df["ma_diff_4"] = df["diff_1"].rolling(window=4, min_periods=4).mean()
med = df["power"].median()

df["day_step"] = df["t"] % 96
good = (
    (df["ma_diff_4"] >= 3)
    & (df["ma_8"] >= med)
    & (df["day_step"] >= 36)
    & (df["day_step"] <= 84)
)
answer = good.sum()
print(answer)
