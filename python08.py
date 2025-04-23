import random
import math

# 4번. 1 이상 10 이하 정수 5개를 저장하는 리스트
scores = [random.randint(1, 10) for _ in range(5)]
print("Scores:", scores)

# 5번. 리스트 scores의 합계
total = sum(scores)
print("Sum:", total)

# 6번. 리스트 scores의 평균
average = total / len(scores)
print("Average:", average)

# 7번. 리스트 scores의 분산
variance = sum((x - average) ** 2 for x in scores) / len(scores)
print("Variance:", variance)

# 8번. 리스트 scores의 표준편차
dev = math.sqrt(variance)
print("Standard Deviation:", dev)

# 9번. 리스트 scores에서 최댓값
maximum = max(scores)
print("Max:", maximum)

# 10번. 리스트 scores에서 최솟값
minimum = min(scores)
print("Min:", minimum)
