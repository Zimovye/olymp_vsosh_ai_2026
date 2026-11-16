from pathlib import Path
import pandas as pd

# Зачем так сложно, если можно просто `df=pd.read_csv("tests.csv")`?
df = pd.read_csv(Path(__file__).with_name("group_by_var3_task4.csv"), encoding="utf-8")
# Какие ещё наиболее частые методы pandas мне могут пригодиться? (.fillna(), .clip(), .replace(), .mean(), .mode(), .groupby())
df["score"] = df["score"].fillna(0)
# Что такое .loc?
# ```
# mask_neg = d f [ " s c o r e " ] < 0
# d f . l o c [ mask_neg , " s c o r e " ] = 0
# ```
df["score"] = df["score"].clip(0, 100)

good = (~df["cheat_flag"]) & (df["attempt_no"] == 1)
df = df[good].copy()

mean_by_student = df.groupby("student_id")["score"].mean()
good = (mean_by_student >= 60) & (mean_by_student < 80)
print(good.sum())
