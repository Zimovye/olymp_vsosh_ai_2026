n = 9
time_limit = 24

s_all = []
strategies = []
for number in range(3**n):
    strategy = []

    for position in range(n - 1, -1, -1):
        action = (number // 3**position) % 3
        strategy.append(action)

    K = 0
    T = 0
    hs = []

    for action in strategy:
        if action == 2:
            h_curr = min(1.5 + 0.25 * K, 5)
            K += 1
            T += 4
        elif action == 1:
            h_curr = min(3 + 0.5 * K, 5)
            K += 0.5
            T += 2
        else:
            h_curr = 4.5
            T += 1
        hs.append(h_curr)

    if T > time_limit:
        continue

    E = min(1 + 0.5 * K, 5)
    H = sum(hs) / len(hs)
    S = 0.4 * H + 0.6 * E
    s_all.append(S)
    strategies.append(strategy)

Smax = max(s_all)
best_strategies = [strat for strat, s in zip(strategies, s_all) if s == Smax]
amount = len(best_strategies)
the_bestest = min(best_strategies)

print(f"{Smax:.3f}")
print(amount)
print("".join(map(str, the_bestest)))
