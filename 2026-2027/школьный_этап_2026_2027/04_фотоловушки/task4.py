from collections import Counter

file = open("camera_traps.csv", encoding="utf-8")

file.readline()

data: list[tuple[int, int, str]] = []
for line in file:
    camera_id, timestamp, animal, confidence = line.strip().split(",")
    confidence = 0 if not confidence else float(confidence)
    if confidence >= 0.8:
        time = timestamp.split(":")
        time = int(time[1])
        data.append((int(camera_id), time, animal))
variety = len(set(i[2].lower() for i in data))
print("Кол-во уникальных:", variety)

visits: dict[tuple[str, int], int] = {}
best_cameras = Counter()
sorted_data = sorted(data, key=lambda x: x[1])
for camera_id, time, animal in sorted_data:
    if abs(visits.setdefault((animal, camera_id), time) - time) > 10:
        best_cameras[camera_id] += 1

m = max(best_cameras.values())
print([cam for cam, v in best_cameras.items() if v == m])
print(m)
