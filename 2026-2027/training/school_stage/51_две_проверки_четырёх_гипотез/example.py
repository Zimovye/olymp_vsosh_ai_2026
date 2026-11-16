# Учебный уменьшенный пример: нужно различить три возможных правила.
# Все три правила подходят для исходной тройки (1, 2, 3).
#
# Правило 1: числа строго возрастают.
# Правило 2: все числа положительные.
# Правило 3: подходят любые три числа.

test_1 = (-1, 0, 1)
test_2 = (-1, -1, -1)

# Каждое правило получает два ответа: сначала для test_1, затем для test_2.
rule_1_answers = (
    test_1[0] < test_1[1] < test_1[2],
    test_2[0] < test_2[1] < test_2[2],
)

rule_2_answers = (
    test_1[0] > 0 and test_1[1] > 0 and test_1[2] > 0,
    test_2[0] > 0 and test_2[1] > 0 and test_2[2] > 0,
)

# Правило «подходят любые три числа» всегда отвечает «да».
rule_3_answers = (True, True)

print("Проверка 1:", test_1)
print("Проверка 2:", test_2)
print()
print("Правило 1 — строго возрастают:", rule_1_answers)
print("Правило 2 — все положительные:", rule_2_answers)
print("Правило 3 — любые три числа:", rule_3_answers)

pairs_are_different = (
    rule_1_answers != rule_2_answers
    and rule_1_answers != rule_3_answers
    and rule_2_answers != rule_3_answers
)
print("Все пары ответов различны:", pairs_are_different)
print()
print("Правильный ответ учебного примера — две тройки:")
print(test_1)
print(test_2)
