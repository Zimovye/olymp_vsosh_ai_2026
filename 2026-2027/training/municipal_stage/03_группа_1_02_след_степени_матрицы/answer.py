power = 20

p, q, r, s = 1, 1, 1, 0
for k in range(2, power + 1):
    new_p = p + q
    new_q = p
    new_r = r + s
    new_s = r
    p, q, r, s = new_p, new_q, new_r, new_s

print(p + s)
