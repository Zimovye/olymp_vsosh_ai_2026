n = int(input())

objects = []
for _ in range(n):
    number = int(input())
    bits = format(number, "010b")
    objects.append(bits)

answer = 0
idxs: list[int] = []
seen = set()

for feature in range(10):
    first = objects[0][feature]
    curr_bits = []
    is_found = False

    for bits in objects:
        curr_bits.append(bits[feature])
        if bits[feature] != first:
            is_found = True

    if is_found:
        curr_bits_col = "".join(curr_bits)
        if curr_bits_col not in seen:
            seen.add(curr_bits_col)
            idxs.append(feature + 1)
            answer += 1

if answer != 0:
    print(answer, " ".join(map(str, idxs)))
else:
    print(0)
