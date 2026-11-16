n = int(input())

objects = []
for i in range(n):
    number = int(input())
    bits = format(number, "010b")
    objects.append(bits)

answer = 0
for feature in range(10):
    first = objects[0][feature]
    changes = False

    for bits in objects:
        if bits[feature] != first:
            changes = True
            break

    if changes:
        answer += 1

print(answer)
