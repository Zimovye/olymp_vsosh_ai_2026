devices = 12
channels = 12

max_groups = 0
for groups in range(1, devices + 1):
    if devices % groups != 0:
        continue
    group_size = devices // groups
    min_channels = groups * (group_size - 1)
    max_channels = groups * (group_size * (group_size - 1) // 2)
    if min_channels <= channels <= max_channels:
        max_groups = groups
print(max_groups)
