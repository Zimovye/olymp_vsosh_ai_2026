from fractions import Fraction
from itertools import permutations

correct_variant = [1, 2, 3, 4]
all_variants = list(permutations(correct_variant))

good = 0
for var in all_variants:
    matches = 0
    for pos in range(len(correct_variant)):
        if var[pos] == correct_variant[pos]:
            matches += 1
    if matches == 1:
        good += 1

pred = Fraction(good, len(all_variants))
print(pred)
