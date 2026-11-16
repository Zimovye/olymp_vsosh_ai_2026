# Элемент с индексом 0 не используем: номера вершин на схеме начинаются с 1.
p = [0] + list(map(int, input().split()))
paths = []

for number in range(8):
    code = format(number, "03b")
    node = 1
    probability = 1
    visited = []

    for bit in code:
        visited.append(node)
        # По нумерации схемы дети вершины node имеют номера 2*node и 2*node+1.
        if bit == "0":
            probability *= p[node]
            node = 2 * node
        else:
            probability *= 100 - p[node]
            node = 2 * node + 1

    paths.append((probability, code))
    print(code, "Вершины:", visited, "Числитель вероятности:", probability)

paths.sort()

print("Ответ:")
for probability, code in paths:
    print(code)
