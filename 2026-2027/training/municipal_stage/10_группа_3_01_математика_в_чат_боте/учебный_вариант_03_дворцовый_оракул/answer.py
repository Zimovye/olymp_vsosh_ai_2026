from collections import Counter

L, R = map(int, input().split(" "))

m_cnt = Counter()
for a in range(2, R + 1):
    b = 1
    while a**b - a * b <= R:
        correct = a**b
        model = a * b
        if L <= correct - model <= R:
            m_cnt[model] += 1
        b += 1

if m_cnt:
    m = max(m_cnt.values())
    print(min(k for k, v in m_cnt.items() if v == m), m)
else:
    print("0 0")
