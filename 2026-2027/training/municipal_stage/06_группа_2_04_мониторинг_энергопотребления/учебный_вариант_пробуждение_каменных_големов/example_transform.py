import pandas as pd

# Маленький поясняющий пример, не данные и не решение основной задачи.
small = pd.DataFrame({
    "golem_id": [3, 11, 3, 11, 3, 11],
    "charge": [10, 100, 14, 104, 18, 108],
})

print("Исходные строки:")
print(small)

print("Обычная median: одно значение на голема")
print(small.groupby("golem_id")["charge"].median())

# Строка median — имя операции, которую transform выполняет для каждой группы.
small["med"] = small.groupby("golem_id")["charge"].transform("median")


def average_two(s):
    # s содержит весь столбец charge одного голема, с исходными номерами строк.
    print("В функцию передали одну группу:")
    print(s)
    return s.rolling(window=2, min_periods=2).mean()


small["ma_2"] = small.groupby("golem_id")["charge"].transform(average_two)

# Та же операция в короткой записи, как в твоём коде:
# small["ma_2"] = small.groupby("golem_id")["charge"].transform(
#     lambda s: s.rolling(window=2, min_periods=2).mean()
# )

print("transform вернул результаты к их исходным строкам:")
print(small)
