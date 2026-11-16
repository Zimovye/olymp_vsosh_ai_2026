from pathlib import Path
import pandas as pd
import numpy as np


# 1. df — вся таблица. Первая строка CSV станет названиями столбцов.
df = pd.read_csv(Path(__file__).with_name("orders_train.csv"), encoding="utf-8")
print("Первые пять заказов:")
print(df.head())
print("Всего заказов:", len(df))


# 2. Сравниваем время сразу у всех заказов: получаем столбец True/False.
# Для двух таких столбцов нужен &, а каждое сравнение заключаем в скобки.
valid_hours = (df["delivery_hours"] >= 1) & (df["delivery_hours"] <= 96)
print("Какие из первых пяти заказов оставляем:")
print(valid_hours.head())

# df[valid_hours] оставляет строки с True. Копию можно изменять отдельно.
df = df[valid_hours].copy()
print("После фильтрации осталось заказов:", len(df))


# 3. read_csv обычно уже распознаёт пустые ячейки как пропуски NaN.
# Как в исходном разборе, учитываем и пустые строки, если они остались.
df["label"] = df["label"].replace("", np.nan)

# mode() игнорирует пропуски и возвращает столбец самых частых значений.
# В обоих наших файлах мода единственная; iloc[0] берёт первое значение.
modes = df["label"].mode()
print("Результат mode():")
print(modes)
mode_label = modes.iloc[0]
print("Мода:", mode_label)

# fillna возвращает заполненный столбец; сохраняем его обратно в таблицу.
df["label"] = df["label"].fillna(mode_label)


# 4. min() и max() работают по всему столбцу рейтингов после фильтрации.
min_rating = df["rating"].min()
max_rating = df["rating"].max()
print("Минимальный рейтинг:", min_rating)
print("Максимальный рейтинг:", max_rating)

# Вычитание и деление выполняются для каждой оценки без нашего цикла.
# В обоих файлах min и max различаются, поэтому знаменатель не равен нулю.
df["rating_norm"] = (df["rating"] - min_rating) / (max_rating - min_rating)
print("Таблица после преобразований (до 12 строк):")
print(df.head(12))


# 5. is_good содержит True только у заказов, прошедших все три проверки.
is_good = (
    (df["label"] == mode_label)
    & (df["rating_norm"] >= 0.8)
    & (df["delivery_hours"] <= 48)
)
print("Первые подходящие заказы:")
print(df[is_good].head())

# При суммировании True считается как 1, False — как 0.
answer = is_good.sum()
print("Ответ:", answer)
