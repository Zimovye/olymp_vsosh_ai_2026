from pathlib import Path
import pandas as pd


df = pd.read_csv(Path(__file__).with_name("tests_train.csv"), encoding="utf-8")
print("Работ в исходной таблице:", len(df))
print(df.head())


# Ошибочные баллы исправляем, а не удаляем вместе с работами.
df["score"] = df["score"].fillna(0)
df["score"] = df["score"].clip(0, 100)

# Среднее должно учитывать только допустимые первые попытки.
df = df[df["cheat_flag"] == False]
df = df[df["attempt_no"] == 1]
print("Работ после отбора:", len(df))
print(df.head(12))


# Собираем работы одного ученика и усредняем его оставшиеся баллы.
mean_by_student = df.groupby("student_id")["score"].mean()
print("Средний балл каждого ученика:")
print(mean_by_student)

# Проверяем средние, поэтому считаем учеников, а не отдельные работы.
good = (mean_by_student >= 60) & (mean_by_student < 80)
print("Подходящие ученики и их средние:")
print(mean_by_student[good])

answer = good.sum()
print("Ответ для учебного файла:", answer)
