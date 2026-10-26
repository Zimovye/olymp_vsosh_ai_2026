# Маленький готовый пример: все группы должны быть одинакового размера.
devices = 8
channels = 6

max_groups = 0

for groups in range(1, devices + 1):
    # Равные группы возможны, только если устройства делятся без остатка.
    if devices % groups != 0:
        continue

    group_size = devices // groups

    # Каждой связной группе нужно хотя бы group_size - 1 каналов.
    min_channels = groups * (group_size - 1)

    # В каждой группе можно соединить напрямую каждую пару устройств.
    max_channels = groups * (group_size * (group_size - 1) // 2)

    print(
        "Групп:", groups,
        "устройств в группе:", group_size,
        "минимум каналов:", min_channels,
        "максимум каналов:", max_channels,
    )

    if min_channels <= channels <= max_channels:
        max_groups = groups

print("Максимальное число равных групп:", max_groups)
