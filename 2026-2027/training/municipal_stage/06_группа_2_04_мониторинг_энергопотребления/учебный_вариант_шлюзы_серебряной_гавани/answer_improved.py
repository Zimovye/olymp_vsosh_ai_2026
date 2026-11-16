from pathlib import Path
import pandas as pd

df = pd.read_csv(Path(__file__).with_name("tide.csv"), encoding="utf-8")

df["diff_1"] = df["level"].diff()

df["ma_8"] = df["level"].rolling(window=8, min_periods=8).mean()

# Усредняем изменения уровня, поэтому берём diff_1, а не сам level.
df["ma_diff_4"] = df["diff_1"].rolling(window=4, min_periods=4).mean()

med = df["level"].median()

df["day_step"] = df["t"] % 96

good_hours = (df["day_step"] >= 36) & (df["day_step"] <= 84)

danger = (df["ma_diff_4"] >= 3) & (df["ma_8"] >= med) & good_hours

cnt = 0
best_len = 0
best_start = 0
best_end = 0
curr_len = 0
for t, d in zip(df["t"], danger):
    if d:
        curr_len += 1
        # На третьем измерении считаем одну тревогу; продолжение её не удваивает.
        if curr_len == 3:
            cnt += 1
            print("Новая тревога, начало:", t - curr_len + 1)

        # Обновляем сразу: серия может закончиться последней строкой файла.
        # Короткие серии не участвуют, а равная длина не вытесняет раннюю тревогу.
        if curr_len >= 3 and curr_len > best_len:
            best_len = curr_len
            best_start = t - curr_len + 1
            best_end = t
    else:
        curr_len = 0

print(cnt)
print(best_start, best_end, best_len)
