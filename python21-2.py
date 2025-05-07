import seaborn as sns
import matplotlib.pyplot as plt

# Load mpg dataset
mpg = sns.load_dataset("mpg").dropna()

# 데이터프레임 출력, 요약 정보, 기술 통계량, 범주형 변수 빈도수
print(mpg.head())
print(mpg.info())
print(mpg.describe())
print(mpg["cylinders"].value_counts())
print(mpg["origin"].value_counts())
print(mpg["model_year"].value_counts())

# mpg ~ displacement 산점도
sns.scatterplot(data=mpg, x="displacement", y="mpg")
plt.title("mpg vs displacement")
plt.show()

# 2x2 subplot: mpg 관계 시각화
fig, axs = plt.subplots(2, 2, figsize=(10, 8))
sns.scatterplot(data=mpg, x="cylinders", y="mpg", ax=axs[0, 0])
axs[0, 0].set_title("mpg vs cylinders")
sns.scatterplot(data=mpg, x="horsepower", y="mpg", ax=axs[0, 1])
axs[0, 1].set_title("mpg vs horsepower")
sns.scatterplot(data=mpg, x="weight", y="mpg", ax=axs[1, 0])
axs[1, 0].set_title("mpg vs weight")
sns.scatterplot(data=mpg, x="acceleration", y="mpg", ax=axs[1, 1])
axs[1, 1].set_title("mpg vs acceleration")
plt.tight_layout()
plt.show()

# 빈도수 막대 그래프
sns.countplot(data=mpg, x="cylinders")
plt.title("Cylinders 빈도수")
plt.show()

sns.countplot(data=mpg, x="origin")
plt.title("Origin 빈도수")
plt.show()

sns.countplot(data=mpg, x="model_year")
plt.title("Model Year 빈도수")
plt.show()

# origin, cylinders 빈도수 (교차)
sns.countplot(data=mpg, x="origin", hue="cylinders")
plt.title("Origin vs Cylinders")
plt.show()

# 통계량 막대 그래프 (중앙값)
mpg.groupby("cylinders")["mpg"].median().plot(kind="bar")
plt.title("Cylinders별 mpg 중앙값")
plt.ylabel("Median mpg")
plt.show()

mpg.groupby("origin")["mpg"].median().plot(kind="bar")
plt.title("Origin별 mpg 중앙값")
plt.ylabel("Median mpg")
plt.show()

# box plot
sns.boxplot(data=mpg, y="mpg")
plt.title("mpg Boxplot")
plt.show()

sns.boxplot(data=mpg, y="displacement")
plt.title("displacement Boxplot")
plt.show()

sns.boxplot(data=mpg, y="weight")
plt.title("weight Boxplot")
plt.show()

sns.boxplot(data=mpg, x="origin", y="mpg")
plt.title("Origin별 mpg Boxplot")
plt.show()

# 히스토그램
sns.histplot(mpg["mpg"], kde=True)
plt.title("mpg Histogram")
plt.show()

sns.histplot(mpg["displacement"], kde=True)
plt.title("Displacement Histogram")
plt.show()

sns.histplot(mpg["weight"], kde=True)
plt.title("Weight Histogram")
plt.show()

sns.histplot(mpg["model_year"])
plt.title("Model Year Histogram")
plt.show()

# pairplot
sns.pairplot(mpg[["mpg", "displacement", "horsepower", "weight", "acceleration"]])
plt.suptitle("mpg 관련 변수 간 관계", y=1.02)
plt.show()
