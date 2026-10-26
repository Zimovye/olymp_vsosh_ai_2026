from fractions import Fraction

# Каждого пользователя система выбирает с одинаковой вероятностью.
probability_choose_user = Fraction(1, 3)

# Вероятность получить «Драконов» через каждого пользователя.
anya_and_dragons = probability_choose_user * 0
boris_and_dragons = probability_choose_user * Fraction(1, 2)
vika_and_dragons = probability_choose_user * Fraction(1, 3)

print("Аня и «Драконы»:", anya_and_dragons)
print("Боря и «Драконы»:", boris_and_dragons)
print("Вика и «Драконы»:", vika_and_dragons)

# Складываем все способы, которыми могли рекомендовать «Драконов».
probability_dragons = anya_and_dragons + boris_and_dragons + vika_and_dragons
print("Вероятность рекомендации «Драконов»:", probability_dragons)

# Среди всех случаев с «Драконами» находим долю случаев с Викой.
answer = vika_and_dragons / probability_dragons
print("Вероятность, что выбрали Вику:", answer)
