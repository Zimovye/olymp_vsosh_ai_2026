from itertools import permutations

a_day = [1, 4, 2, 3]
a_night = [4, 1, 3, 2]
nums = [-2, 1, 3, 6]
all_vars = list(permutations(nums))

g_all = []
for var in all_vars:
    u, v, w, x = var[0], var[1], var[2], var[3]

    # a_day
    p, q, r, s = a_day[0], a_day[1], a_day[2], a_day[3]  # не очень красиво выглядит
    ab_first = p * u + q * w
    ab_second = r * v + s * x
    trace_ab = ab_first + ab_second
    s_day = trace_ab  # не очень красиво выглядит

    # a_night
    p, q, r, s = (
        a_night[0],
        a_night[1],
        a_night[2],
        a_night[3],
    )  # не очень красиво выглядит
    ab_first = p * u + q * w
    ab_second = r * v + s * x
    trace_ab = ab_first + ab_second
    s_night = trace_ab

    g = min(s_day, s_night)
    g_all.append(g)

m = max(g_all)
print(m)
print(len([x for x in g_all if x == m]))
