n = int(input())

objects = []
for i in range(n):
    number = int(input())
    # Нули слева сохраняют одинаковые позиции всех десяти признаков.
    bits = format(number, "010b")
    objects.append(bits)
    if i < 3:
        print(number, "->", bits)

answer = 0
for feature in range(10):
    first = objects[0][feature]
    changes = False

    for bits in objects:
        if bits[feature] != first:
            changes = True
            # Одного отличия достаточно, чтобы оставить этот признак.
            break

    if changes:
        answer += 1
        print("Признак", feature + 1, "— оставляем")
    else:
        print("Признак", feature + 1, "— удаляем")

print("Осталось признаков:", answer)
