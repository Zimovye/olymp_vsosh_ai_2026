from itertools import permutations

nums = [-4, -5, 20, 25]
all_vars = list(permutations(nums))

traces_ab = []
traces_ba = []
for var in all_vars:
    x, y, z, w = var[0], var[1], var[2], var[3]

    ab_first = -1 * x + 4 * z
    ab_second = 5 * y + 10 * w
    trace_ab = ab_first + ab_second
    traces_ab.append(trace_ab)

    ba_first = x * -1 + y * 5
    ba_second = z * 4 + w * 10
    trace_ba = ba_first + ba_second
    traces_ba.append(trace_ba)

print(f"а) {max(traces_ab)}")
print(f"б) {max(traces_ba)}")
