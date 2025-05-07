import seaborn as sns
import matplotlib.pyplot as plt

# Load iris dataset
iris = sns.load_dataset("iris")

# 데이터프레임 일부 출력, 요약 정보, 기술 통계량, 품종 빈도수
print(iris.head())
print(iris.info())
print(iris.describe())
print(iris["species"].value_counts())

# 숫자 타입 컬럼 box plot
iris.select_dtypes(include='number').boxplot()
plt.title("iris 수치 변수 Box Plot")
plt.show()

# 숫자 타입 변수 평균 막대 그래프
iris.select_dtypes(include='number').mean().plot(kind="bar")
plt.title("iris 수치 변수 평균")
plt.ylabel("평균값")
plt.show()

# 품종별 연속형 변수들의 box plot
for col in iris.select_dtypes(include='number').columns:
    sns.boxplot(data=iris, x="species", y=col)
    plt.title(f"{col} by Species")
    plt.show()

# 품종별 연속형 변수들의 평균 막대 그래프
iris.groupby("species").mean().plot(kind="bar")
plt.title("품종별 평균값")
plt.ylabel("평균")
plt.xticks(rotation=0)
plt.show()

# 산점도: petal_width ~ petal_length
sns.scatterplot(data=iris, x="petal_length", y="petal_width", hue="species")
plt.title("Petal Width vs Length (품종별)")
plt.show()

# pairplot
sns.pairplot(iris, hue="species")
plt.suptitle("iris 변수 간 관계 (pairplot)", y=1.02)
plt.show()
