import csv

# CSV 파일에서 데이터 읽기
data = []

# CSV 파일 열기
with open('exam.csv', mode='r') as file:
    reader = csv.reader(file)
    next(reader)  # 첫 번째 줄은 컬럼명이므로 건너뜀
    for row in reader:
        data.append(row)
# 결과 확인
for row in data[:5]:  # 처음 5줄만 출력해서 확인
    print(row)


print('----------------------')
# 2차원 리스트의 모든 값을 정수(int)로 변환
for i in range(len(data)):
    data[i] = [int(value) if value.isdigit() else value for value in data[i]]
# 결과 확인
for row in data[:5]:  # 처음 5줄만 출력해서 확인
    print(row)


print('----------------------')

# 1반 학생들의 수학 점수만 추출
class_1_math_scores = [row[2] for row in data if row[1] == 1]

print(class_1_math_scores[:5])  
# 1반 학생들의 수학 점수 처음 5개만 출력

print('----------------------')


# 수학 점수의 총점, 최댓값, 최솟값, 평균 계산
total_score = sum(class_1_math_scores)
max_score = max(class_1_math_scores)
min_score = min(class_1_math_scores)
average_score = total_score / len(class_1_math_scores)

# 결과 출력
print(f"1반 수학 점수 총점: {total_score}")
print(f"1반 수학 점수 최댓값: {max_score}")
print(f"1반 수학 점수 최솟값: {min_score}")
print(f"1반 수학 점수 평균: {average_score:.2f}")
