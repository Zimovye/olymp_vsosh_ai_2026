weights = [1, 4, 2, 5, 3, 6, 2, 4, 5, 3]
n = len(weights)

answer = []
for number in range(2**n):
    K = 0
    weighted_sum = 0  # Числитель дроби: w1H1+w2H2+...+w10H10/sum(weights)
    strategy = []

    for position in range(n - 1, -1, -1):
        action = (number // (2**position)) % 2
        strategy.append(action)

    for action, weight in zip(strategy, weights):
        if action == 1:
            current_h = 1.5 + 0.3 * K
            K += 1
        else:
            current_h = 4.5
        weighted_sum += current_h * weight

    H = weighted_sum / sum(weights)
    E = min(1 + 0.5 * K, 5)
    S = 0.4 * H + 0.6 * E
    answer.append((S, "".join(map(str, strategy))))  # Как можно сделать лучше?

Smax = max(score for score, _ in answer)
best_strategies = [strategy for score, strategy in answer if score == Smax]
amount = len(best_strategies)
min_strategy = min(best_strategies)

print(f"{Smax:.3f}")
print(amount)
print(min_strategy)
