from pathlib import Path
import pandas as pd

df = pd.read_csv(Path(__file__).with_name("bells.csv"), encoding="utf-8")
# Если бы t не был отсортирован (хотя по усл. он sorted), то чтобы отсортировать мне нужно было бы написать эту строку? Она верная?
# df = df.sort_values("t")
# Можно ли написать df["resonance"].groupby("bell_id").transform(...)? Что будет если так написать?
diff_1 = df.groupby("bell_id")["resonance"].transform(lambda s: s.diff())
ma_8 = df.groupby("bell_id")["resonance"].transform(
    lambda s: s.rolling(window=8, min_periods=8).mean()
)
# Зачем здесь diff_1.groupby(df["bell_id"]), если diff_1 и так уже отгруппирован?
# Почему не `ma_diff_4 = diff_1.groupby("bell_id").transform(...)`?
ma_diff_4 = diff_1.groupby(df["bell_id"]).transform(
    lambda s: s.rolling(window=4, min_periods=4).mean()
)
med = df.groupby("bell_id")["resonance"].transform("median")

df["day_step"] = df["t"] % 96
good_hours = (df["day_step"] >= 36) & (df["day_step"] <= 84)

dangerous = (ma_diff_4 >= 3) & (ma_8 >= med) & good_hours

# Как можно красиво сделать? Я уже запутался в этих длинных названиях.
cnt_bells = {}
stats = {
    "episodes_cnt": 0,
    "curr_cnt_danger": 0,
    "best_cnt_danger": 0,
    "curr_start": 0,
    "best_start": 0,
    "best_end": 0,
    "last_danger": 0,
}
for t, bell_id, d in zip(df["t"], df["bell_id"], dangerous):
    state = cnt_bells.setdefault(bell_id, stats.copy())

    if not d:
        continue

    if t - state["last_danger"] > 2:
        state["curr_cnt_danger"] = 0

    state["curr_cnt_danger"] += 1
    state["last_danger"] = t

    if state["curr_cnt_danger"] == 1:
        state["curr_start"] = t

    if state["curr_cnt_danger"] == 3:
        state["episodes_cnt"] += 1
    if (
        state["curr_cnt_danger"] >= 3
        and state["curr_cnt_danger"] > state["best_cnt_danger"]
    ):
        state["best_cnt_danger"] = state["curr_cnt_danger"]
        state["best_start"] = state["curr_start"]
        state["best_end"] = t

for bell_id, stats in sorted(cnt_bells.items()):
    print(
        bell_id,
        stats["episodes_cnt"],
        stats["best_start"],
        stats["best_end"],
        stats["best_cnt_danger"],
    )
