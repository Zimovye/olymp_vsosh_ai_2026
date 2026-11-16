L, R = map(int, input().split(" "))

seen = set()
for a in range(2, R + 1):
    b = 1
    while a**b - a * b <= R:
        correct = a**b
        model = a * b
        if L <= correct - model <= R:
            seen.add(model)
        b += 1
print(len(seen), sum(seen))
