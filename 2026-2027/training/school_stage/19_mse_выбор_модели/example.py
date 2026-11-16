# Маленький учебный пример: три точки и две модели.
data = [(0, 1), (1, 2), (2, 5)]

squared_errors_1 = []
squared_errors_2 = []

for x, y in data:
    prediction_1 = 2 * x
    prediction_2 = x + 1

    # Возводим разницу в квадрат, чтобы ошибки разных знаков не сократились.
    squared_error_1 = (y - prediction_1) ** 2
    squared_error_2 = (y - prediction_2) ** 2

    squared_errors_1.append(squared_error_1)
    squared_errors_2.append(squared_error_2)

    print("Точка: x =", x, "y =", y)
    print("Модель y = 2x: предсказание =", prediction_1,
          "квадрат ошибки =", squared_error_1)
    print("Модель y = x + 1: предсказание =", prediction_2,
          "квадрат ошибки =", squared_error_2)
    print()

mse_1 = sum(squared_errors_1) / len(data)
mse_2 = sum(squared_errors_2) / len(data)

print("MSE модели y = 2x:", round(mse_1, 3))
print("MSE модели y = x + 1:", round(mse_2, 3))

if mse_1 < mse_2:
    print("Лучшая модель: y = 2x")
else:
    print("Лучшая модель: y = x + 1")
