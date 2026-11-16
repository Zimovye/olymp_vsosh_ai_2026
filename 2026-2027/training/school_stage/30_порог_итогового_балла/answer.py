n = 10
S = -1
correct_honest = []

for honest in range(n + 1):
    K = 0
    Hs = []

    for _ in range(honest):
        h = 1.5 + 0.3 * K
        K += 1
        Hs.append(h)

    for _ in range(n - honest):
        Hs.append(4.5)

    E = min(1 + 0.5 * K, 5)
    avg_hs = sum(Hs) / len(Hs)
    S = 0.4 * avg_hs + 0.6 * E
    if S >= 4.150:
        correct_honest.append(honest)

print(" ".join(map(str, correct_honest)))
print(min(correct_honest))
