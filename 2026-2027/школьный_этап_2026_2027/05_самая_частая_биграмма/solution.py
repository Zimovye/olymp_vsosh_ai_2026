from collections import Counter


n, k = map(int, input().split())
s = input().strip()

counts = Counter()

# Каждая биграмма внутри s встречается в каждой из k копий.
for i in range(n - 1):
    bigram = s[i : i + 2]
    counts[bigram] += k

# Между k копиями есть k - 1 стыков.
if k > 1:
    border_bigram = s[-1] + s[0]
    counts[border_bigram] += k - 1

best_bigram = ""
best_count = -1

# Лексикографическая сортировка сразу ставит меньшие биграммы раньше.
for bigram in sorted(counts):
    if counts[bigram] > best_count:
        best_bigram = bigram
        best_count = counts[bigram]

print(best_bigram)
print(best_count)
