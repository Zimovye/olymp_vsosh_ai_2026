import pandas as pd
from collections import defaultdict

df = pd.read_csv("knights.csv", encoding="utf-8")

df["score"] = df["score"].fillna(0)

df["score"] = df["score"].clip(0, 100)

all_orders = sorted(set(df["order_id"]))

# mask_min = df["score"] < 0
# df.loc[mask_min, "score"] = 0
# mask_max = df["score"] >= 100
# df.loc[mask_max, "score"] = 100

good = (~df["cheat_flag"]) & (df["attempt_no"] == 1)

df = df[good].copy()

# В ключе остаются и орден, и рыцарь: среднее не потеряет своего владельца.
mean_knights = df.groupby(["order_id", "knight_id"])["score"].mean()
print("Средние баллы: орден, рыцарь, среднее")
print(mean_knights)

cnt_knight = defaultdict(list)
# items берёт ключ (орден, рыцарь) вместе с относящимся к нему средним.
for (order_id, knight_id), mean_score in mean_knights.items():
    if 60 <= mean_score < 80:
        pair = (knight_id, mean_score)
        cnt_knight[order_id].append(pair)


total_knights = 0
for order_id in all_orders:
    # Пары начинаются с номера рыцаря, поэтому меньшие номера идут первыми.
    pairs = sorted(cnt_knight[order_id])
    print("Орден", order_id, "подходящие рыцари:", pairs)

    # Если список пуст, цикл ниже не выполнится и знаменосцем останется 0.
    best_knight = 0
    best_score = -1
    for knight_id, mean_score in pairs:
        # При равных средних сохраняем меньший номер, встреченный раньше.
        if mean_score > best_score:
            best_knight = knight_id
            best_score = mean_score

    print(order_id, len(pairs), best_knight)
    # В общем итоге считаются все подходящие рыцари, а не только знаменосцы.
    total_knights += len(pairs)

print(total_knights)
