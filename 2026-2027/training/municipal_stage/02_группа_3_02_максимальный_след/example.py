from itertools import permutations


# Учебное изменение исходной задачи:
# A = (1 2)
#     (3 4)
# Числа для B — 1, 2, 3, 4.
numbers = [1, 2, 3, 4]
all_vars = list(permutations(numbers))
traces_ab = []
traces_ba = []

for var in all_vars:
    x, y, z, w = var[0], var[1], var[2], var[3]

    # Для следа нужны только верхняя левая и нижняя правая клетки произведения.
    ab_first = x + 2 * z
    ab_second = 3 * y + 4 * w
    trace_ab = ab_first + ab_second

    ba_first = x + 3 * y
    ba_second = 2 * z + 4 * w
    trace_ba = ba_first + ba_second

    print("B:", var, "Диагональ AB:", (ab_first, ab_second),
          "tr(AB):", trace_ab, "tr(BA):", trace_ba)

    traces_ab.append(trace_ab)
    traces_ba.append(trace_ba)

print("Максимальный tr(AB):", max(traces_ab))
print("Максимальный tr(BA):", max(traces_ba))
