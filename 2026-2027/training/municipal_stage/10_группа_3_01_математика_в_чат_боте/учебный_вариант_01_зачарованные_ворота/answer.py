L, R = map(int, input().split(" "))

C = 0
S = 0
for a in range(2, R + 1):
    b = 1
    while a**b - a * b <= R:
        correct = a**b
        model = a * b
        if L <= correct - model <= R:
            C += 1
            S += model
        b += 1
print(C, S)
