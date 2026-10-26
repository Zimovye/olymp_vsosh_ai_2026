point_1 = (-1, 2)
point_2 = (1, 0)

# Я уверен это можно сделать как-то красиво с помощью функций?
rules_1 = (
    point_1[0] > 0,
    point_2[0] > 0,
)
rules_2 = (
    point_1[1] > 0,
    point_2[1] > 0,
)
rules_3 = (
    point_1[0] + point_1[1] > 0,
    point_2[0] + point_2[1] > 0,
)
rules_4 = (
    point_1[0] * point_1[1] > 0,
    point_2[0] * point_2[1] > 0,
)
tests = [point_1, point_2]
rules = [rules_1, rules_2, rules_3, rules_4]
for i, rule in enumerate(rules):
    if not rule[0] and not rule[1]:
        print(i + 1)
