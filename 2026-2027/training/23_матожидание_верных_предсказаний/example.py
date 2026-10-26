# Маленький учебный пример: четыре предсказания «зелёный».
green_probability = 0.4
prediction_count = 4

expected_correct = 0

for prediction_number in range(1, prediction_count + 1):
    # Каждое предсказание добавляет вероятность того, что оно окажется верным.
    expected_correct += green_probability
    print("После предсказания", prediction_number,
          "математическое ожидание равно", expected_correct)

print("Ожидаемое число верных предсказаний:", expected_correct)
