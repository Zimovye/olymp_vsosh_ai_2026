k = int(input())

# Восемь карт для генерации всегда дают общее число карт, кратное восьми.
for generate in range(1, 9):
    update = k * generate
    total = generate + update

    print("Генерация:", generate, "Обновление:", update, "Всего карт:", total)
    print("Остаток при делении на 8:", total % 8)

    if total % 8 == 0:
        nodes = total // 8
        print("Минимальное число нод:", nodes)

        # Число карт растёт, поэтому первый подходящий вариант уже минимален.
        break
