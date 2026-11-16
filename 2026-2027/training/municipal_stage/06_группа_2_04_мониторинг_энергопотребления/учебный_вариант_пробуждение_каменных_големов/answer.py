from pathlib import Path
import pandas as pd

df = pd.read_csv(Path(__file__).with_name("golems.csv"), encoding="utf-8")
diff_1 = df.groupby("golem_id")["charge"].diff()
# Я всё равно не понял. Объяни ещё подробнее.
ma_8_g = df.groupby("golem_id")["charge"].transform(
    lambda s: s.rolling(window=8, min_periods=8).mean()
)
ma_diff_4_g = diff_1.groupby(df["golem_id"]).transform(
    lambda s: s.rolling(window=4, min_periods=4).mean()
)

# "median" же не функция, это строка
med = df.groupby("golem_id")["charge"].transform("median")

df["day_step"] = df["t"] % 96
good_hours = (df["day_step"] >= 36) & (df["day_step"] <= 84)
is_danger = (ma_diff_4_g >= 3) & (ma_8_g >= med) & good_hours

# Как-то я тут запутанно сделал. Сам же через день забуду, что это, или нет. Может можно как-то лучше сделать?
cnt_golems = {}  # golem_id: [cnt, best_len, best_start, best_end, curr_len]
for t, golem_id, d in zip(df["t"], df["golem_id"], is_danger):
    if d:
        cnt_golems.setdefault(golem_id, [0, 0, 0, 0, 0])[4] += 1  # curr_len
        if cnt_golems[golem_id][4] == 3:  # curr_len
            cnt_golems[golem_id][0] += 1  # cnt
        if (
            cnt_golems[golem_id][4] >= 3
            and cnt_golems[golem_id][4] > cnt_golems[golem_id][1]  # curr_len > best_len
        ):
            cnt_golems[golem_id][1] = cnt_golems[golem_id][4]  # best_len = curr_len
            cnt_golems[golem_id][2] = (
                t - cnt_golems[golem_id][4] + 1
            )  # best_start = t - curr_len + 1
            cnt_golems[golem_id][3] = t  # best_end
    else:
        cnt_golems.setdefault(golem_id, [0, 0, 0, 0, 0])[4] = 0  # curr_len
for golem_id, (cnt, best_len, best_start, best_end, _) in sorted(cnt_golems.items()):
    print(golem_id, cnt, best_start, best_end, best_len)
