import pandas as pd
import seaborn as sns

# tips 데이터셋 로드
tips = sns.load_dataset('tips')
print(type(tips))
tips

# 1. DataFrame의 row, column 개수
print("1. 행과 열의 개수:", tips.shape)

# 2. 컬럼 이름
print("\n2. 컬럼 이름:", tips.columns.tolist())

# 3. 첫 5개 행
print("\n3. 첫 5개 행:")
print(tips.head())

# 4. 마지막 5개 행
print("\n4. 마지막 5개 행:")
print(tips.tail())

# 5. 요약 정보
print("\n5. 요약 정보:")
print(tips.info())

# 6. 숫자 타입 변수들의 기술 통계량
print("\n6. 숫자 타입 기술 통계량:")
print(tips.describe())

# 7. 카테고리 변수들의 빈도수
print("\n7. 카테고리 변수 빈도수:")
for col in ['sex', 'smoker', 'day', 'time']:
    print(f"\n[{col}]")
    print(tips[col].value_counts())

# 8. total_bill 최댓값인 행
print("\n8. total_bill 최댓값인 행:")
print(tips[tips['total_bill'] == tips['total_bill'].max()])

# 9. total_bill 최솟값인 행
print("\n9. total_bill 최솟값인 행:")
print(tips[tips['total_bill'] == tips['total_bill'].min()])

# 10. 남성의 팁 평균
male_tip_mean = tips[tips['sex'] == 'Male']['tip'].mean()
print(f"\n10. 남성 팁 평균: {male_tip_mean:.2f}")

# 11. 여성의 팁 평균
female_tip_mean = tips[tips['sex'] == 'Female']['tip'].mean()
print(f"11. 여성 팁 평균: {female_tip_mean:.2f}")

# 12. 일요일 팁 평균
sunday_tip_mean = tips[tips['day'] == 'Sun']['tip'].mean()
print(f"12. 일요일 팁 평균: {sunday_tip_mean:.2f}")

# 13. 일요일, 남성 팁 평균
sunday_male_tip_mean = tips[(tips['day'] == 'Sun') & (tips['sex'] == 'Male')]['tip'].mean()
print(f"13. 일요일 남성 팁 평균: {sunday_male_tip_mean:.2f}")

# 14. 일요일, 여성 팁 평균
sunday_female_tip_mean = tips[(tips['day'] == 'Sun') & (tips['sex'] == 'Female')]['tip'].mean()
print(f"14. 일요일 여성 팁 평균: {sunday_female_tip_mean:.2f}")
