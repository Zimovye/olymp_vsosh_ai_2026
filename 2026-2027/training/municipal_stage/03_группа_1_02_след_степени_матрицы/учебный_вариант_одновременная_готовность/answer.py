power = 30
p, q, r, s = 2, 1, 3, 1
u, v, w, x = 3, 1, 1, 1

for n in range(2, power + 1):
    new_p = p * 2 + q * 3
    new_q = p * 1 + q * 1
    new_r = r * 2 + s * 3
    new_s = r * 1 + s * 1
    p, q, r, s = new_p, new_q, new_r, new_s

    new_u = u * 3 + v * 1
    new_v = u * 1 + v * 1
    new_w = w * 3 + x * 1
    new_x = w * 1 + x * 1
    u, v, w, x = new_u, new_v, new_w, new_x

    det_a = p + s
    det_b = u + x

    if det_a >= 5000 and det_b >= 5000:
        print(n, det_a, det_b)
        break
