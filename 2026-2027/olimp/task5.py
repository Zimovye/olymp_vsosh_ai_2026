from sys import stdin
from collections import Counter

n, k = map(int, stdin.readline().strip().split(" "))
s = stdin.readline().strip()


t = s * k
bigrams = []
for i in range(len(t)):
    if i == len(t) - 1:
        break
    bigram = t[i] + t[i + 1]
    bigrams.append(bigram)

cnt = Counter(bigrams)
m = max(cnt.values())
best = [b for b, v in cnt.items() if v == m]
ans = sorted(best)[0]
print(ans)
print(m)
