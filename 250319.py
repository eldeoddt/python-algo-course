# 실전 예제 2
'''
v = int(input("주행 속도 : "))
t = int(input("주행 시간 : "))
print("주행 이동 거리 : ", v*t)
'''

# 실전 예제 01 - 수온 계산기
# 해수면에서 10m내려갈 때마다 수온이 0.7도씩 내려간다.
# 수심 입력하면 수온을 계산한다.
depth = int(input("수심을 입력하세요. "))
print("수온 : ", 20 - ( (depth // 10) * 0.7) )

# 실전 예제 03 - 시험 합격 판단
# 3과목 시험. 과목당 10문제, 배점 1점.
# 총 30점 중 20점 이상이어야 합격.
# 각 과목은 6점 이상이어야 합격.
# 입력
exam1 = int(input("첫 번째 시험 점수를 입력하세요. "))
exam2 = int(input("두 번째 시험 점수를 입력하세요. "))
exam3 = int(input("세 번째 시험 점수를 입력하세요. "))

#판단
total = exam1+exam2+exam3
isSuccess = (total > 19) & (exam1 > 5) & (exam2 > 5) & (exam3 > 5)

# 출력
print("시험 점수 총합 : ", total)
print("당신은 시험에 %s 했습니다." %(isSuccess))
print(f"당신은 시험에 {isSuccess} 했습니다.") # 포매팅
