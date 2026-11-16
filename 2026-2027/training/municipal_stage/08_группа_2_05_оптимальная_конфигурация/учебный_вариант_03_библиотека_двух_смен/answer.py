k1, k2, r, B = map(int, input().split(" "))

is_found = False
for writers in range(1, 8 * B + 1):
    painters = writers * k1
    total_1 = writers + painters + r

    if total_1 % 8 == 0 and (halls_1 := total_1 // 8) <= B:
        if (total_1 - r) % (k2 + 1) == 0:
            translators = (total_1 - r) // (k2 + 1)
            bookbinders = translators * k2
            print(halls_1, writers, painters, translators, bookbinders)
            is_found = True
            break

if not is_found:
    print(-1)
