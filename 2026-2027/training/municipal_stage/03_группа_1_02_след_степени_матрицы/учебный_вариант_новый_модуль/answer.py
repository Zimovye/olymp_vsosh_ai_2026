power = 30
p, q, r, s = 2, 1, 3, 1

for n in range(2, power + 1):
    new_p = p * 2 + q * 3
    new_q = p * 1 + q * 1
    new_r = r * 2 + s * 3
    new_s = r * 1 + s * 1
    p, q, r, s = new_p, new_q, new_r, new_s
    det = p + s
    if det >= 5000:
        print(n, det)
        break
