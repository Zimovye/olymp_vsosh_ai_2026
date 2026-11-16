from pathlib import Path
import pandas as pd

# Вариант без ручного подсчёта серий — по вопросу из answer.py.
df = pd.read_csv(Path(__file__).with_name("tide.csv"), encoding="utf-8")

df["diff_1"] = df["level"].diff()
df["ma_8"] = df["level"].rolling(window=8, min_periods=8).mean()
df["ma_diff_4"] = df["diff_1"].rolling(window=4, min_periods=4).mean()
med = df["level"].median()
df["day_step"] = df["t"] % 96
good_hours = (df["day_step"] >= 36) & (df["day_step"] <= 84)
danger = (df["ma_diff_4"] >= 3) & (df["ma_8"] >= med) & good_hours

df["danger"] = danger
# В каждой строке увидим признак из предыдущей. До начала ряда опасности нет.
df["previous"] = danger.shift(fill_value=False)
# Новый номер нужен каждый раз, когда True меняется на False или наоборот.
df["new_series"] = danger != df["previous"]
# При True прибавляется 1, при False остаётся прежний номер серии.
df["series_id"] = df["new_series"].cumsum()

print("Как появляются номера серий:")
print(df[["t", "danger", "previous", "new_series", "series_id"]].iloc[34:40])

# Номера уже рассчитаны по всему ряду. Теперь можно оставить опасные строки:
# разорванные серии сохранят разные номера.
alarms = df[danger].groupby("series_id")["t"].agg(["min", "max", "count"])
print("Все опасные серии: начало, конец, число измерений")
print(alarms)

alarms = alarms[alarms["count"] >= 3]
# Сначала большая длина, при равенстве — меньший номер начала.
alarms = alarms.sort_values(["count", "min"], ascending=[False, True])

print(len(alarms))
if len(alarms) == 0:
    print(0, 0, 0)
else:
    best = alarms.iloc[0]
    print(best["min"], best["max"], best["count"])
