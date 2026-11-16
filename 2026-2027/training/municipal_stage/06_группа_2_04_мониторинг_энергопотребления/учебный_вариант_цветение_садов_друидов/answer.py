from pathlib import Path
import pandas as pd

df = pd.read_csv(Path(__file__).with_name("gardens.csv"), encoding="utf-8")
diff_1 = df.groupby("garden_id")["bloom"].transform(lambda x: x.diff())
ma_8 = df.groupby("garden_id")["bloom"].transform(
    lambda x: x.rolling(window=8, min_periods=8).mean()
)
ma_diff_4 = diff_1.groupby(df["garden_id"]).transform(
    lambda x: x.rolling(window=4, min_periods=4).mean()
)
med = df.groupby("garden_id")["bloom"].transform("median")

df["day_step"] = df["t"] % 96
good_hours = (df["day_step"] >= 36) & (df["day_step"] <= 84)
dangerous = (ma_diff_4 >= 3) & (ma_8 >= med) & good_hours

# print(df.groupby("garden_id")["ma_diff_4"].head()), почему он не выводит сгруппированную таблицу?

cnt_episodes = {}
# Опять много получилось. Все ли они нужны?
stats = {
    "cnt_active": 0,
    "best_strength": 0,
    "best_len": 0,
    "best_start": 0,
    "best_end": 0,
    "curr_strength": 0,
    "curr_start": 0,
    "curr_active": 0,
    "last_t": 0,
}
for t, garden_id, m, is_d in zip(df["t"], df["garden_id"], ma_diff_4, dangerous):
    stat = cnt_episodes.setdefault(garden_id, stats.copy())

    if not is_d:
        continue

    # Один неактивный момент между активными разрешён; два или больше подряд разделяют эпизоды
    if t - stat["last_t"] > 2:
        stat["curr_strength"] = 0
        stat["curr_active"] = 0

    stat["last_t"] = t

    if stat["curr_active"] == 0:
        stat["curr_start"] = t

    stat["curr_active"] += 1

    if stat["curr_active"] == 3:
        stat["cnt_active"] += 1

    # Почему мы берём, в формуле (x_t) - (x_t-4) число на 4 позиции раньше, то есть в окне всего получается 5 чисел,
    # хотя ma_diff_4 берёт окно из 4 чисел? Ничего не понимаю.
    stat["curr_strength"] += 4 * m  # Сразу вклад активного элемента

    if stat["curr_strength"] > stat["best_strength"] and stat["curr_active"] >= 3:
        stat["best_strength"] = stat["curr_strength"]
        stat["best_start"] = stat["curr_start"]
        stat["best_end"] = t
        stat["best_len"] = stat["curr_active"]

for garden_id, stat in sorted(cnt_episodes.items()):
    print(
        garden_id,
        stat["cnt_active"],
        stat["best_start"],
        stat["best_end"],
        stat["best_len"],
        int(stat["best_strength"]),
    )
