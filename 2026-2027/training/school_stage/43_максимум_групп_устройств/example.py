# Маленький готовый пример: 6 устройств и 3 канала.
devices = 6
channels = 3

group_size = 1

while group_size * (group_size - 1) // 2 < channels:
    capacity = group_size * (group_size - 1) // 2
    print("Устройств в большой группе:", group_size, "Вмещается каналов:", capacity)
    group_size += 1

capacity = group_size * (group_size - 1) // 2
single_devices = devices - group_size
max_groups = 1 + single_devices

print("Минимальный размер большой группы:", group_size)
print("В неё помещается каналов:", capacity)
print("Одиночных устройств:", single_devices)
print("Максимальное число групп:", max_groups)
