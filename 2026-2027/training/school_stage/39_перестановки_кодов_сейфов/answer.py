from fractions import Fraction
from itertools import permutations

correct_order = [1, 2, 3, 4]
all_variants = list(permutations(correct_order))

good = 0
for var in all_variants:
    matches = 0
    for pos in range(len(correct_order)):
        if var[pos] == correct_order[pos]:
            matches += 1
    if matches > 0:
        good += 1

pred = Fraction(good, len(all_variants))
print(pred)
