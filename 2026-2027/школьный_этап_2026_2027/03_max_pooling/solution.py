def max_pooling(sequence):
    result = []
    for index in range(len(sequence) - 1):
        pair_maximum = max(sequence[index], sequence[index + 1])
        result.append(pair_maximum)
    return result


pooled = [1, 3, 3, 2, 4, 4]

# Из первых двух пар однозначно получаем x2 = 1 и x3 = 3.
# Из пятой пары получаем x6 = 4, потому что x5 не больше 2.
# Для x4 и x5 возможны разные значения, если их максимум равен 2.
first_sequence = [0, 1, 3, 2, 1, 4, 0]
second_sequence = [0, 1, 3, 1, 2, 4, 0]

print("Первый возможный вариант:", first_sequence)
print("После max-pooling:", max_pooling(first_sequence))

print("Второй возможный вариант:", second_sequence)
print("После max-pooling:", max_pooling(second_sequence))

ambiguous_positions = []
for index in range(len(first_sequence)):
    if first_sequence[index] != second_sequence[index]:
        ambiguous_positions.append(index + 1)

print("Неоднозначные позиции:", ambiguous_positions)
print("Количество неоднозначных чисел:", len(ambiguous_positions))
