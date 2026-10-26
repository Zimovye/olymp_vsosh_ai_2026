file = open("data.csv", encoding="utf-8")
file.readline()

counts = 0
prev_signal = int(file.readline().strip().split(",")[1])
for line in file:
    signal = int(line.strip().split(",")[1])
    if abs(signal - prev_signal) >= 5:
        counts += 1
    prev_signal = signal

file.close()

print(counts)
