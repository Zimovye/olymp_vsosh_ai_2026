k, r = map(int, input().split(" "))

is_found = False
for painters in range(1, 9):
    chekans = painters * k
    total = painters + chekans + r
    if total % 8 == 0:
        halls = total // 8
        print(halls, painters, chekans)
        is_found = True
        break

if not is_found:
    print(-1)
