'''
# 01 편의점 재고 관리하기
proddict = {}
while(True):
    prod = input("입력 물품 ==> ")
    if(prod == 'z'):
        break
    amount = int(input("재고량 ==> "))
    proddict[prod] = amount

print("*** 물품의 재고량 확인 ***")
while(True):
    find = input("찾을 물품 ==> ")
    if (find == ""):
        break
    if find in proddict:
        print(f"{proddict[find]} 개 남았어요")
    else:
        print("그 물품은 없어요.")

# 02 100일 기념일 날짜 구하기
# 현재 시간 구하기
from datetime import datetime, timedelta
now = datetime.now()
print(f"현재 날짜와 시간\t\t==> {now}")
# 현재 시간부터 일정 날짜가 지난 후의 날짜 구하기
after = now + timedelta(days=100)
print(f"100일 후 날짜와 시간\t==> {after}")

# 03 비밀번호 생성하기
while(True):
    npw = input("새로운 비밀번호를 입력하세요 : ")

    validate = True
    for i in npw:
        for j in "!@#$%^&*()":
            if i == j:
                validate = False

    if(len(npw)>=8 and validate):
        print("Good~ 비밀번호가 올바르게 생성되었어요")
        break
    else:
        print("오류! 비밀번호가 규칙에 맞지 않습니다")
'''

# 04 퀴즈
# 문제 입력
quiz = (
    ["도둑이 가장 좋아하는 아이스크림은?", "누가바", 4],
    ["차도가 없는 나라는?", "인도", 3],
    ["오리가 얼면?", "언덕", 3],
    ["들어갈때는 1000명 나올 때는 100명인 곳은?", "인천 아웃백", 5],
    ["1+1의 정답을 중국 사람이 말하면?", "이다해", 5]
)

# 채점하기
score = []
for i in range(len(quiz)):
    print(f"문제 {i + 1} : {quiz[i][0]} ")
    ans = input("정답 : ")
    if ans == quiz[i][1]:
        score.append(1)
print('-'*10 + "채점" + "-"*10)
sum = 0
for i in range(len(score)):
    print(f"{i+1}번 : ", end="")
    if score[i] == 1 :
        print(f"정답 +{quiz[i][2]}")
        sum += quiz[i][2]
    else:
        print("오답")

print(f"최종 점수 : {sum}")
