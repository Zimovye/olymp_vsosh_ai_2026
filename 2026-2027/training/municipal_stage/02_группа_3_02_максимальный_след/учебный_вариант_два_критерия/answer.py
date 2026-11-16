from itertools import permutations

nums = [-2, 1, 3, 6]
all_vars = list(permutations(nums))
a_day = [1, 4, 2, 3]
a_night = [5, 4, 3, 1]

g_all: list[tuple[int, int]] = []
for var in all_vars:
    u, v, w, x = var[0], var[1], var[2], var[3]

    # day
    p, q, r, s = a_day[0], a_day[1], a_day[2], a_day[3]
    ab_first = p * u + q * w
    ab_second = r * v + s * x
    trace_ab = ab_first + ab_second
    s_day = trace_ab

    # night
    p, q, r, s = a_night[0], a_night[1], a_night[2], a_night[3]
    ab_first = p * u + q * w
    ab_second = r * v + s * x
    trace_ab = ab_first + ab_second
    s_night = trace_ab

    g = min(s_day, s_night)
    t = s_day + s_night
    g_all.append((g, t))

max_g = max([g for g, _ in g_all])
max_t = max([t for g, t in g_all if g == max_g])
# amount = sum([1 for g, t in g_all if g == max_g and t == max_t])
amount = g_all.count((max_g, max_t))

print(max_g)
print(max_t)
print(amount)
