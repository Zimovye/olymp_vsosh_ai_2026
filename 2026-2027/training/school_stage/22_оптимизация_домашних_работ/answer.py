homework_n = 10

S = -1
best_honest = 0

for honest in range(homework_n + 1):
    K = 0
    H = 0

    for _ in range(honest):
        H += 1.5 + 0.3 * K
        K += 1

    for _ in range(homework_n - honest):
        H += 4.5

    E = min(1 + 0.5 * K, 5)
    final_score = 0.4 * H / 10 + 0.6 * E

    if final_score > S:
        S = final_score
        best_honest = honest

print(round(S, 3))
print(best_honest)
