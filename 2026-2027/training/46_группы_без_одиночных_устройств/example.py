# Маленький готовый пример: одиночные устройства запрещены.
devices = 8
channels = 6

max_groups = 0

# В каждой группе должно быть хотя бы два устройства.
for groups in range(1, devices // 2 + 1):
    # Для наибольшей вместимости оставляем groups - 1 пар,
    # а все остальные устройства помещаем в одну большую группу.
    largest_group = devices - 2 * (groups - 1)

    # Связной группе из t устройств нужно хотя бы t - 1 каналов.
    min_channels = devices - groups

    # В большой группе проводим все возможные каналы,
    # а в каждой из оставшихся пар помещается один канал.
    max_channels = largest_group * (largest_group - 1) // 2 + (groups - 1)

    print(
        "Групп:",
        groups,
        "минимум каналов:",
        min_channels,
        "максимум каналов:",
        max_channels,
    )

    if min_channels <= channels <= max_channels:
        max_groups = groups

print("Максимальное число групп:", max_groups)
