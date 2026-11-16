# Открываем маленький учебный CSV из папки этой задачи.
file = open("data.csv", encoding="utf-8")
print(f"Чтение самого файла: {file}")

# Первая строка содержит названия столбцов p,y, поэтому пропускаем её.
first_row = file.readline()
print(first_row)

data = []

for line in file:
    # line = line.strip()
    p_text, y_text = line.strip().split(",")

    p = float(p_text)
    y = int(y_text)
    data.append((p, y))

file.close()

print("Загруженные строки:", data)
print("Количество строк:", len(data))

correct = 0

for p, y in data:
    # Равенство 0.6 входит в условие, поэтому используем >=.
    if p >= 0.6:
        prediction = 1
    else:
        prediction = 0

    is_correct = prediction == y
    print("p =", p, "y =", y, "предсказание =", prediction, "совпало =", is_correct)

    if is_correct:
        correct += 1

print("Количество правильных предсказаний:", correct)
