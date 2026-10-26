devices = 12
channels = 10

max_groups = 0
for groups in range(1, devices // 2 + 1):
    largest_group = devices - 2 * (groups - 1)
    min_channels = devices - groups
    max_channels = largest_group * (largest_group - 1) // 2 + (groups - 1)

    if min_channels <= channels <= max_channels:
        max_groups = groups
print(max_groups)
