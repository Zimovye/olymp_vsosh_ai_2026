from fractions import Fraction

# 0 - blue; 1 - red
chances = {0: Fraction(2, 3), 1: Fraction(1, 3)}
predoctions = [0, 0, 0]

counts = 0
for pred in predoctions:
    counts += chances[pred]

print(counts)
