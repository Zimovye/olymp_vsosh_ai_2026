point_1 = (-1, 2)
point_2 = (1, 0)
points = (point_1, point_2)


# Каждая функция получает одну точку и проверяет одно правило.
def rule_1(x, y):
    return x > 0


def rule_2(x, y):
    return y > 0


def rule_3(x, y):
    return x + y > 0


def rule_4(x, y):
    return x * y > 0


# Функции можно хранить в наборе так же, как другие значения.
rules = (rule_1, rule_2, rule_3, rule_4)

for number, rule in enumerate(rules, start=1):
    answers = []

    for x, y in points:
        answers.append(rule(x, y))

    print("Правило", number, "даёт ответы", answers)

    if answers == [False, False]:
        print("Ответ:", number)
