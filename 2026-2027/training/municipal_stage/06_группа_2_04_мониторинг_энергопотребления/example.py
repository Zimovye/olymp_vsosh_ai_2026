import pandas as pd

df = pd.read_csv("power_train.csv", encoding="utf-8")

# Порядок строк важен: сравниваем соседние показания по времени.
df["diff_1"] = df["power"].diff()

# min_periods требует полное окно. Первые неполные окна останутся NaN.
df["ma_8"] = df["power"].rolling(window=8, min_periods=8).mean()
df["ma_diff_4"] = df["diff_1"].rolling(window=4, min_periods=4).mean()

print("Начало ряда: видны первые полные окна")
print(df.head(10))

# Медиану берём по всей мощности, до отбора по времени и другим условиям.
med = df["power"].median()
print("Медиана мощности:", med)

# В каждых сутках 96 показаний. Остаток возвращает позицию внутри суток.
df["day_step"] = df["t"] % 96
in_hours = (df["day_step"] >= 36) & (df["day_step"] <= 84)

good = (df["ma_diff_4"] >= 3.0) & (df["ma_8"] >= med) & in_hours
df["good"] = good

print("Переход через медиану: сравни строки 46 и 47")
print(df[(df["t"] >= 45) & (df["t"] <= 48)])
print("Граница времени: сравни строки 84 и 85")
print(df[(df["t"] >= 83) & (df["t"] <= 86)])

print("Первые подходящие моменты второго дня")
print(df[good & (df["t"] >= 96)].head(3))

answer = int(good.sum())
print("Ответ:", answer)
