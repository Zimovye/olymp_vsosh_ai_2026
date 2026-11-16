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
mean_knights = df.groupby(["order_id", "knight_id"])["score"].mean()
print(mean_knights)


cnt_knight = defaultdict(list)
# "Hashable" не является итерируемым
#   Метод "__iter__" не определенPylancereportGeneralTypeIssues
# (variable) knight_id: Unknown
for (order_id, knight_id), mean_score in mean_knights.items():
    if 60 <= mean_score < 80:
        pair = (knight_id, mean_score)
        cnt_knight[order_id].append(pair)

total_knight = 0
for order_id in all_orders:
    best_knight = 0
    best_score = -1
    for knight_id, mean in cnt_knight[order_id]:
        if mean > best_score:
            best_knight = knight_id
            best_score = mean
    print(order_id, len(cnt_knight[order_id]), best_knight)
    total_knight += len(cnt_knight[order_id])
print(total_knight)
