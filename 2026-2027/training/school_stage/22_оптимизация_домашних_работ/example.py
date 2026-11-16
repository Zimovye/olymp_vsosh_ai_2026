# Маленький учебный пример с пятью домашними заданиями.
homework_count = 5

S = -1
best_honest_count = 0

for honest_count in range(0, homework_count + 1):
    knowledge = 0
    homework_grades = []

    # Для h самостоятельных работ знания перед ними равны 0, 1, ..., h - 1.
    for _ in range(honest_count):
        grade = 2 + 0.5 * knowledge
        homework_grades.append(grade)
        knowledge += 1

    # Остальные работы списаны и не меняют знания.
    for _ in range(homework_count - honest_count):
        homework_grades.append(5)

    average_homework = sum(homework_grades) / homework_count
    exam_grade = min(1 + knowledge, 4)
    final_score = 0.4 * average_homework + 0.6 * exam_grade

    if final_score > S:
        S = final_score
        best_honest_count = honest_count

print("Максимальный итоговый балл:", round(S, 3))
print("Оптимальное число самостоятельных работ:", best_honest_count)
