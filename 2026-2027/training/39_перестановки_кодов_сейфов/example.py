from fractions import Fraction
from itertools import permutations


# Маленький готовый пример: три кода должны попасть к трём сейфам.
correct_order = [1, 2, 3]
all_variants = list(permutations(correct_order))
good_variants = 0

for variant in all_variants:
    matches = 0

    for position in range(len(correct_order)):
        if variant[position] == correct_order[position]:
            matches += 1

    print("Вариант:", variant, "Совпадений:", matches)

    # Подходит любое распределение хотя бы с одним верным кодом.
    if matches > 0:
        good_variants += 1

total_variants = len(all_variants)
probability = Fraction(good_variants, total_variants)

print("Подходящих вариантов:", good_variants)
print("Всего вариантов:", total_variants)
print("Вероятность:", probability)
