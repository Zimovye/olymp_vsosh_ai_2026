# 1: числа строго возрастают;
# 2: все числа положительные;
# 3: подходят любые три числа;
# 4: произведение первого и последнего чисел равно квадрату второго.

test_1 = (1, 2, 4)
test_2 = (1, 2, 3)
test_3 = (-3, -3, -3)
test_4 = (-3, -2, -1)

rule_1 = (
    test_1[0] < test_1[1] < test_1[2],
    test_2[0] < test_2[1] < test_2[2],
    test_3[0] < test_3[1] < test_3[2],
    test_4[0] < test_4[1] < test_4[2],
)
rule_2 = (
    test_1[0] > 0 and test_1[1] > 0 and test_1[2] > 0,
    test_2[0] > 0 and test_2[1] > 0 and test_2[2] > 0,
    test_3[0] > 0 and test_3[1] > 0 and test_3[2] > 0,
    test_4[0] > 0 and test_4[1] > 0 and test_4[2] > 0,
)
rule_3 = (True, True, True, True)
rule_4 = (
    test_1[0] * test_1[2] == test_1[1] ** 2,
    test_2[0] * test_2[2] == test_2[1] ** 2,
    test_3[0] * test_3[2] == test_3[1] ** 2,
    test_4[0] * test_4[2] == test_4[1] ** 2,
)
tests = [test_1, test_2, test_3, test_4]
rules = [rule_1, rule_2, rule_3, rule_4]

for first in range(len(tests)):
    for second in range(first + 1, len(tests)):
        answer_pairs = []
        for rule in rules:
            answer_pairs.append((rule[first], rule[second]))
        if len(set(answer_pairs)) == len(set(rules)):
            print(tests[first], tests[second])
