from collections import Counter
from datetime import datetime

file = open("camera_traps.csv", encoding="utf-8")

file.readline()

data = []
for line in file:
    camera_id, timestamp, animal, confidence = line.strip().split(",")
    confidence = 0 if not confidence else float(confidence)
    if confidence >= 0.8:
        time = datetime.fromisoformat(timestamp)
        data.append((int(camera_id), time, animal))
variety = len(set(i[2].lower() for i in data))
print("Кол-во уникальных:", variety)

visits = {}
best_cameras = Counter()
sorted_data = sorted(data, key=lambda x: (x[0], x[2], x[1]))
for camera_id, time, animal in sorted_data:
    pair = (animal, camera_id)

    if pair not in visits or (time - visits[pair]).total_seconds() > 10 * 60:
        best_cameras[camera_id] += 1

    visits[pair] = time

m = max(best_cameras.values())
print([cam for cam, v in best_cameras.items() if v == m])
print(m)
