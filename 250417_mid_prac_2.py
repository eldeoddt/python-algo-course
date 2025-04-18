## 04 연산자
'''
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
'''

## 05 조건문
'''
# 양의 정수 3으로 나눈 후 소수점 첫자리에서 반올림한 정수를 출력하기. 2:14-2:24     10분
# 실수에서 버림은 int()함수로도 가능 하다!
n = int(input("양의정수 입력  "))
fnum = n / 3
remain = fnum - (n // 3)
if (remain >= 0.5):
    fnum = (n // 3) + 1
else:
    fnum = (n // 3)
print(f"{fnum}")

# bmi 지수 입력 받기 2:32 - 2:38                  6분
bmi=float(input("bmi 지수 입력  "))
if(bmi>140):
    print("고도비만")
elif(bmi>120):
    print("비만")
elif(bmi>110):
    print("과체중")
elif(bmi>90):
    print("정상 체중")
else:
    print("저체중")

# 마스크 구매 가능 요일 출력 2:39-42                 3분
year=int(input("출생연도끝자리입력   "))
age=int(input("만나이 입력   "))
if(age>=65):
    print("언제든지구매가능")
else:
    if(year==1 or year==6):
        print("월요일 구매")
    elif(year==2 or year==7):
        print("화요일 구매")
    elif(year==3 or year==8):
        print("수요일 구매")
    elif(year==4 or year==9):
        print("목요일 구매")
    elif(year==5 or year==0):
        print("금요일 구매")
'''

'''
# 배수 판별하기 5:36 - 38                           2분
n = int(input("정수  "))
if((n%3==0) & (n%5==0)):
    print("3과 5의 배수임")
else:
    print("3과 5의 배수 아님")

# 차량 2부제 프로그램 5:45-48                       3분
num = int(input("차번호 4자리  "))
date = int(input("오늘날짜  "))
if(date%2==0):
    print("오늘입차: 번호짝수차량")
    if(num%2!=0):
        print("입차불가")
    else:print("입차가능")
else:
    print("오늘입차: 번호홀수차량")
    if (num % 2 == 0):
        print("입차불가")
    else:
        print("입차가능")

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

# BMI 계산기 6:05-6:16                          11분
name = (input("이름 입력 ; "))
m = float(input("키 입력 ; "))
kg = float(input("몸무게 입력 ; "))

bmi = kg /(m*m*0.0001)
if(bmi > 30): string="고도비만"
elif(bmi >= 25): string="비만"
elif(bmi >= 23): string="과체중"
elif(bmi >=18.5 ): string="정상"
else:string="저체중"
print(f"{name}님의 키는 {m:.0f}cm이고, 몸무게는 {kg:.0f}kg입니다.\nbmi지수는 {bmi:.2f}입니다. {string}입니다.")

# 윤년 계산 6:20-23                                3분
y = int(input("연도입력  "))
if(((y%4==0)&(y%100!=0)) | (y%400==0)):
    print(f"{y}년은 윤년입니다.")
else:
    print(f"{y}년은 윤년이 아닙니다.")
'''

## 06 반복문
'''
# 50보다 작은 7의 배수 출력하기            1분
for i in range(1, 50, 1):
    if(i%7==0):print(i)

# 에어컨 온도 희망온도 도달시 종료하기        10분
temp=float(input("희망온도  "))
cur=30.0
print("냉방기능 동작")
while(cur>temp):
    print(f"현재온도  {cur}")
    cur-=0.1
print("희망온도 도달. 종료합니다.")

# 삼각형 넓이 구하기 7:01-7:11                  10분
w = 1
h = 1
cnt=1
s= 0
while(True):
    s=w*h/2
    if(s > 150): break
    print(f"넓이: {s}")
    w=cnt*2
    h=cnt*3
    cnt+=1

# 1부터 100까지 숫자 중 5 또는 7의 배수를 제외한 나머지 정수를 출력하는 프로그램을 만드시오.    20분
# 7:15 - 21
for i in range(1, 101, 1):
    if((i%5==0) or (i%7==0)):
        continue
    print(i)
for i in range(1, 101, 1):
    if((i%5!=0) and (i%7!=0)):
        print(i)

# 왼쪽 과 동일한 결과가 나오게 하시오    1분
num=0
while(True):
    if(num==30):break
    print(num)
    num+=1

# 구구단 2-9단 출력하기 7:42-46
for i in range (1, 10, 1):
    for j in range(2, 10, 1):
        print(f"{j} x {i} = {i*j}", end='\t\t')
    print()

# 별찍기 - *가 트리 모양으로 출력될 수 있도록 하시오. 7:47- 8:39
n = 6
for i in range(1, n + 1, 1):
    # 5 4 3 2 1
    for k in range(n-i, 0, -1):
        print("5", end='')
    #1 2 3 4 5 6
    for j in range(0, i*2-1, 1):
        print("*", end='')
    print()

# 별찍기 - * 가 트리 모양, 숫자 증가하시오. 8:41-8:45                  4분
n=5
cnt=1
for i in range (0, n+1, 1):
    for j in range(n-i-1, 0, -1):
        print(" ", end='')
    for k in range(0, (i+1), 1):
        print(f"{cnt}", end=' ')
        cnt+=1
    print()

# 별찍기 - 다이아몬드 숫자 출력하기. 8:47-57             10분
n=4
cnt=1
for i in range(0, n, 1):
    for j in range(n-i-1, 0, -1):
        print("0", end='')
    for k in range(0, i+1, 1):
        print(f"{cnt}", end=' ')
        cnt+=1
    print()
i, j, k=0, 0, 0
n=3
cnt=6
for i in range(0, n, 1):
    for j in range(0, i+1, 1):
        print("0", end='')
    for k in range(n-i, 0, -1):
        print(f"{cnt}", end=' ')
        cnt-=1
    print()
'''

'''
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

# 대회 평가 점수 구하기 1:55-2:01                   6분
# 최고점만 구한다. 중복 상관없이.
n = 5
scr = [0,0,0,0,0]
max=0
sum = 0
for i in range(0, n, 1):
    scr[i] = int(input(f"심사위원{i+1} 평가점수  "))
    print(scr)
    if scr[i]>max:
        max=scr[i]
    sum+=scr[i]
print((sum-max)/(n-1))

# 심박수 구하기 2:02-2:06                           4분
age=int(input("나이  "))
num=int(input("안정시심박수  "))
target=0
for i in range(40, 90, 10):
    target = ((220-age)-num)*(i/100) + num
    print(f"강도{i}%  목표심박수:{target:.1f}bpm")
'''
