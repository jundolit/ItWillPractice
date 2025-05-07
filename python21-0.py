import seaborn as sns
import matplotlib.pyplot as plt

# 데이터셋 로드
tips = sns.load_dataset("tips")

# 연습문제 1: 요일별 팁 평균 막대 그래프 (흡연여부=행, 시간=열)
g1 = sns.catplot(
    data=tips,
    x="day", y="tip",
    kind="bar",
    row="smoker", col="time",
    estimator="mean", ci=None
)
g1.fig.suptitle("연습문제 1: 요일별 팁 평균 (흡연여부=행, 시간=열)", y=1.03)

# 연습문제 2: 요일별, 성별 팁 평균 막대 그래프 (흡연여부=행, 시간=열)
g2 = sns.catplot(
    data=tips,
    x="day", y="tip", hue="sex",
    kind="bar",
    row="smoker", col="time",
    estimator="mean", ci=None
)
g2.fig.suptitle("연습문제 2: 요일+성별 팁 평균 (흡연여부=행, 시간=열)", y=1.03)

# 연습문제 3: 요일별 팁의 box plot (흡연여부=행, 시간=열)
g3 = sns.catplot(
    data=tips,
    x="day", y="tip",
    kind="box",
    row="smoker", col="time"
)
g3.fig.suptitle("연습문제 3: 요일별 팁 분포 Box Plot (흡연여부=행, 시간=열)", y=1.03)

plt.show()
