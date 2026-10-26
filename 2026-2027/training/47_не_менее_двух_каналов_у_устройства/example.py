# Маленький готовый пример.
# У каждого устройства должно быть не меньше двух каналов.
devices = 9
channels = 10

max_groups = 0

# В каждой группе должно быть хотя бы три устройства.
for groups in range(1, devices // 3 + 1):
    # Для наибольшей вместимости оставляем groups - 1 треугольников,
    # а остальные устройства помещаем в одну большую группу.
    largest_group = devices - 3 * (groups - 1)

    # Цикл через все устройства даёт каждому по два канала.
    min_channels = devices

    # В большой группе проводим все возможные каналы,
    # а в каждом из оставшихся треугольников есть по три канала.
    max_channels = largest_group * (largest_group - 1) // 2 + 3 * (groups - 1)

    print(
        "Групп:", groups,
        "минимум каналов:", min_channels,
        "максимум каналов:", max_channels,
    )

    if min_channels <= channels <= max_channels:
        max_groups = groups

print("Максимальное число групп:", max_groups)
