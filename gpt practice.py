# 수온 계산기 5:07-5:10                        3분
depth=int(input("수심을 입력: "))
# 해수면에서 10m 내려갈때마다 0.7도씩 내려감.
# 0-9 -> 20
temp=20 - ((depth//10) * 0.7)
print(f"수온: {temp:.1f}")

# 자동차 주행 거리 계산기                        2분
# 거리=속력*시간
v = int(input("주행 속도 : "))
t = int(input("주행 속도 : "))
print(f"주행 이동거리: ", v*t)

# 시험 합격 판단 5:12 -18                      4분
# if없이 연산자만으로도 true/false를 만들 수 있다. 비교 연산자 사용 .
first =int(input("첫번째 시험점수 입력: "))
second = int(input("두번째 시험점수 입력: "))
third = int(input("세번째 시험점수 입력: "))
sum = first+second+third
result = (sum > 19) & (first>5) & (second>5) & (third>5)
print("시험점수 총합" , sum)
print(f"당신은 {result}했습니다.")

# 369 게임 만들기 1:21-31                        10분
for i in range(1, 100, 1):
    print(f"{i}", end=' ')
    # 3, 6, 9가 들어가는 경우 출력
    # 1자리 경우 -> 3으로 나누어지면
    if (i < 10 and i % 3 == 0):
        print("짝!", end='')
    # 2자리 경우 -> 10의 자리가 3으로 나누어떨어지거나 일의 자리가 3으로 나누어떨어지는 경우.
    # 50 같은 경우 10으로 나눈 나머지가 0이라서 따로 처리해야 한다.
    if (i > 9 and (i % 10 != 0) and ((i // 10) % 3 == 0 or (i % 10) % 3 == 0)):
        print("짝!", end='')
    if (i % 10 == 0 and (i // 10) % 3 == 0):
        print("짝!", end='')
    print()

# 열차 교차 시간 알아내기 1:33-43                    10분
# 3개 노선. 오전 9시-18시 교차 운행. 교차 시간 구하기.
# 18-9=9. 9*60=540. 총 540분이다. -> 나누어떨어지는 경우 해당 역에 정차함.
a, b, c = 10, 25, 30
for i in range(1, 541, 1):
    if ((i % a == 0) and (i % b == 0)):
        print(f"{9 + (i // 60)}시 {i % 60}분")
    elif ((i % b == 0) and (i % c == 0)):
        print(f"{9 + (i // 60)}시 {i % 60}분")
    elif ((i % a == 0) and (i % c == 0)):
        print(f"{9 + (i // 60)}시 {i % 60}분")

# 로그인 기능 만들기 1:47-54                        7분
cnt = 0
real = "hjs"
while (True):
    pw = input("관리자 암호 입력  ")
    if (pw != real):
        print("암호 다시 확인!")
        cnt += 1
        # cnt 5회 집계가 안된다.-> continue 사용에 주의하자.
        if (cnt >= 5):
            print("로그인 실패! 횟수초과 !")
            break
    if (pw == real):
        print("로그인됏습니다.")
        break

# 생존율 출력 프로그램 5:49-56                         7분
time = int(input("장비사용까지 걸린시간입력  "))
if(time > 360):
    rate=25
elif(time>300):
    rate=25
elif(time>240):
    rate=47
elif(time>180):
    rate=57
elif(time>120):
    rate=66
elif(time>60):
    rate=76
else: rate=85

print(f"생존율:{rate}")

# 전기 요금 계산기 5:57-6:04                         7분
use=float(input("전기 사용량 입력"))
stdfee=0.0
if(use > 400):
    stdfee=280.6
    origin = 7300
elif(use> 200):
    stdfee=187.9
    origin = 1600
else:
    stdfee=99.3
    origin = 910

elecfee=origin + (use*stdfee)
print(f"샤용량: {use}kwh")
print(f"기본요금 : {origin}")
print(f"단가: {stdfee}원")
print(f"전기요금: {elecfee}원")

# 문제 8 장학금 지급 조회
# 1학기 수료, 8학기 넘으면 안됨, 한 학기 이수 학점이 15보다 낮으면 안됨.
# 4 이상이면 전액
# 3.5 이상 - 50%
# 3 이상 - 30%
# 3안되면 받을 수 없다.
print("\n[문제 8]")
scholar = [0, 0, 0]
sem = int(input("현재까지 이수한 학기를 입력하세요. "))
if ((sem <= 1) | (sem > 7)):
    print("장학금 지급 대상이 아닙니다.")
else:
    for i in range(sem):
        credit = int(input(f"{i + 1}번째 학기 이수 학점을 입력하세요. "))
        if (credit <= 15):
            print("장학금 대상이 아닙니다.")
            continue

        avg = float(input(f"{i + 1}번째 학기 이수 평점을 입력하세요. "))

        if (avg >= 4):
            print("전액 장학금!")
            scholar[0] += 1
        elif (avg >= 3.5):
            print("50% 장학금!")
            scholar[1] += 1
        elif (avg >= 3):
            print("30% 장학금!")
            scholar[2] += 1
        else:
            print("장학금 대상이 아닙니다.")
    print("===================")
    print("현재까지 장학금 횟수")
    print(f"전액 장학금 {scholar[0]}회\n50% 장학금 {scholar[1]}회\n30% 장학금 {scholar[2]}회")
    print("===================")

# 문제 9 다이아몬드 출력
print("\n[문제 9]")
n = 10
m = 7
for i in range(1, n, 2):
    # 공백
    for j in range(int((n - i) / 2), 0, -1):
        print(" ", end='')
    # *
    for k in range(i):
        print("*", end='')
    print()
for i in range(m, 0, -2):
    # 공백
    for j in range(0, int((n - i) / 2), 1):
        print(" ", end='')
    # *
    for k in range(i):
        print("*", end='')
    print()

# 문제 10 숫자 피라미드
# 사용자로부터 양의 정수 n 입력, 1부터 숫자 증가시키며 피라미드 출력.
print("\n[문제 10]")
num = int(input("숫자 피라미드의 높이를 입력하세요: "))
cnt = 1
for i in range(0, num, 1):
    # 공백
    for j in range((num - i - 1), 0, -1):
        print(" ", end='')

    # 숫자
    for k in range(0, i + 1, 1):
        print(cnt, end=' ')
        cnt += 1
    print()

# 문제 11 비밀번호 생성
print("\n[문제 11]")
cnt = 0
special = False
while (True):
    str = input("비밀 번호를 입력하세요 ")
    cnt += 1
    if (len(str) < 6):
        print("비밀번호의 길이가 짧습니다.")
        continue
    for i in str:
        if (i in ["!", "@"]):
            special = True
            break
    if (special == True): break
    print("특수문자(! 또는 @) 포함되어야 합니다.")

print("올바른 암호 입니다.")
print(f"귀하의 비밀번호는 {str} 이며 시도한 횟수는 {cnt} 입니다.")
