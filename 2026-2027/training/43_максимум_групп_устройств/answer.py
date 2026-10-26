devices = 10
channels = 10

t = 1  # t - group_size
while t * (t - 1) // 2 < channels:
    capacity = t * (t - 1) // 2
    print("Устройств в большой группе:", t, "Вмещается каналов:", capacity)
    t += 1

capacity = t * (t - 1) // 2
print("Устройств в большой группе:", t, "Вмещается каналов:", capacity)
singles = devices - t
max_groups = 1 + singles
print(max_groups)
