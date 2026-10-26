devices = 12
channels = 14

max_groups = 0
for groups in range(1, devices // 3 + 1):
    largest_group = devices - 3 * (groups - 1)
    min_channels = devices
    max_channels = largest_group * (largest_group - 1) // 2 + 3 * (groups - 1)

    if min_channels <= channels <= max_channels:
        max_groups = groups

print(max_groups)
