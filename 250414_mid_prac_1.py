# 다시 풀어보기
## 04 연산자 ##
# 1 수온 계산기 1분
d = int(input("수심 입력  "))
temp= 20-(d//10)*0.7
print(f"수온: {temp:.1f}")

# 2 자동차 주행 거리 계산기 2
v=int(input("주행속도"))
t = int(input("주행시간"))
print("주행 이동 거리: ", v*t)

# 3 시험 합격 판단 3분
f = int(input("첫 시험점수 입력 "))
s = int(input("두번째 시험점수 입력 "))
t = int(input("세번째 시험점수 입력 "))
sum=f+s+t
print("시험점수 총합: " , sum)
print(f"당신은 시험에 {sum>=20 and f>=6 and s>=6 and t>=6}했습니다")

## 05 조건문 ##
# # 1 배수 판별하기 1분
# n=int(input("정수 "))
# if(n%3==0 and n%5==0):
#     print("3과 5의 배수")
# else:
#     print("3과 5의 배수 아님")
#
# # 2 차량 2부제 프로그램 15-18        3분
# n = int(input("차번호 4자리"))
# day=int(input("오늘날짜"))
# if (day%2==0):
#     print("오늘입차: 번호짝수차")
#     if(n%2==0):
#         print('입차가능')
#     else:
#         print("입차불가")
# else :
#     print("오늘입차: 번호홀수차")
#     if(n%2!=0):
#         print("입차가능")
#     else:
#         print("입차불가")
#
# # 3 생존율 출력 19-22     3분
# sec=int(input("초 입력"))
# rate=0
# if(sec>360):
#     rate=25
# elif(sec>240):
#     rate=47
# elif(sec>180):
#     rate=57
# elif(sec>120):
#     rate=66
# elif(sec>60):
#     rate=76
# elif(sec<=60):
#     rate=85
# print(f"생존율: {rate}%")
#
# # 4 전기요금계산기23-26       3분
#     use=int(input("전기 사용량입력 "))
#     if(use>400):
#         fee=280.6
#         originfee=7300
#         elec=originfee+fee*use
#     elif(use>200):
#         fee=187.9
#         originfee=1600
#         elec=originfee+fee*use
#     elif(use<=200):
#         fee=99.3
#         originfee=910
#         elec=originfee+fee*use
#     print(f'사용량: {use} kwh')
#     print(f'기본요금: {originfee:.1f}원')
#     print(f'단가: {fee:.0f}원')
#     print(f'전기요금: {elec:.1f}원')
#
# # 5 bmi 계산기 28-32       4분
# name=input("이름")
# h = int(input("키 "))
# kg = int(input("몸무게 "))
# bmi=kg/ ((h*0.01)*(h*0.01))
# if(bmi>30):
#     state='고도비만'
# elif(bmi>=25):
#     state="비만"
# elif(bmi>=23):
#     state="과체중"
# elif(bmi>=18.5):
#     state="정상"
#
# print(f"{name}님의 키는 {h}cm이고 몸무게는 {kg}kg입니다. \nBmi 지수는 {bmi:.2f}입니다. {state}입니다.")

# 6 윤년 계산 2분
y=int(input("연도 입력 "))
if(y%4==0 and y%100!=0) or y%400==0:
    print(f'{y}년은 윤년입니다.')
else:
    print(f"{y}년은 윤년이 아닙니다.")

## 06 반복문 ##
# # 1 369 게임 21-33        12분
# for i in range(1, 100, 1):
#     print(i, end=' ')
#     if(i<10 and i%3==0):# 10이하
#         print("짝!", end='')
#     #10 이상, 10으로 나눈나머지 0, 첫자리가 3으로 나눈나머지가 0
#     elif(i>=10 and i%10==0 and (i//10)%3==0):
#         print("짝!", end='')
#     # 10 이상, 10으로 나눈 나머지 0아님, 첫자리 또는 둘째자리가 3으로 나눠떨어짐
#     elif(((i%10)%3==0 or (i//10)%3==0) and i%10!=0):
#         print("짝!", end='')
#     print()
# # 2. 열차 교차 시간 알아내기 41-44         3분
# a=10
# b=25
# c=30
# for i in range(1, 541, 1):
#     if (i%a==0 and i%b==0):
#         print(f"{i//60+9}시 {i%60}분")
#     elif(i%b==a and i%c==0):
#         print(f"{i//60+9}시 {i%60}분")
#     elif(i%a==0 and i%c==0):
#         print(f"{i//60+9}시 {i%60}분")
#
# #3. 로그인 기능만들기 8:45- 9분
# cnt = 0
# real = "hjs"
# while (True):
#     pw = input("관리자 암호 입력  ")
#     if (pw != real):
#         cnt += 1
#         if (cnt >= 5):
#             print("로그인 실패! 횟수초과 !")
#             break
#         print("암호 다시 확인!")
#
#     if (pw == real):
#         print("로그인됏습니다.")
#         break
# # 5 심박수 구하기 58-02       4분
# age = int(input("나이"))
# num=int(input("안정심박수"))
# for i in range(4, 9, 1):
#     target=((220-age)-num)*(i*10/100) + num
#     print(f"강도 {i*10}%  목표 심박수: {target:.1f} bpm")

## 07 반복문 & 조건문 ##
## 1 배수 더하기 57-59   2분
# print("\n[문제 1]")
# sum=0
# for i in range(1, 101, 1):
#     if(i%4==0 and i%6!=0 and i!=24):
#         sum+=i
# print(sum)
#
# # 2 소수 구하기 00-06         6분
# print("\n[문제 2]")
# n=int(input("정수입력  "))
# # 1과 자기 자신으로만 나누어 떨어지는 수. 다른 수로는 나누어지면 안된다.
# isTrue=False
#
# for i in range(2, n, 1): # n-1까지 반복돌아야함.
#     if(n%i==0):
#         isTrue=True # 나누어떨어지면 소수가아님.
#         break
# if(n<=1):
#     print("1보다 큰 수를 입력하세요")
# elif(isTrue):
#     print(f"{n}은 소수가 아닙니다..")
# else:
#     print(f"{n}은 소수입니다..")
#
#
# # 3 2 또는 3의 배수 5:07 09     2분
# print("\n[문제 3]")
# sum = 0
# n = int(input("양의정수 입력  "))
# for i in range(1, n+1, 1): # n도 포함해야 하는것에 주의한다.
#     if(i%2==0 or i%3==0):
#         print(i, end=' ')
#         sum+=i
# print()
# print(f'합계: {sum}')
#
# # 4  조건의 수 구하기   10-13       3분
# print("\n[문제 4]")
# n=1
# sum=0
# while(True):
#     if(n%2!=0 or (n%3==0 and n%2==0)):
#         sum+=n
#     if(sum>1000): break
#     n+=1
# print(f'1000을 넘는 숫자 {n}\n그때까지의합 {sum}')
#
# # 5 자릿수의 합 구하기  5:13-15         2분
# print("\n[문제 5]")
# n = int(input("정수: "))
# o = n//100
# t = (n//10)%10
# th = n%10
# print(o+t+th)
#
# # 문자열 풀이       2분
# nn=input("정수: ")
# sum=0
# for i in nn:
#     sum+=int(i)
# print(sum)
#
# # 6 온도 17-21       4분
# print("\n[문제 6]")
# fir=int(input("초기 온도  "))
# las=int(input("목표 온도  "))
# cnt=0
# while(True):
#     #10% 감소하기
#     fir = fir - (fir*10/100)
#     cnt += 1
#     if(fir <=las):
#         break
# print(f"{cnt} 회 후 온도는 {fir}도이며 목표에 도달합니다.")
#
# # 7 문자 메시지 요금 계산하기 7:01-7         6분
# print("\n[문제 7]")
# print("회원 등급 선택")
# level=int(input("1.vvip, 2.vip, 3.gold "))
# sms = int(input("sms"))
# mms = int(input("mms"))
# smsprice = 0
# mmsprice = 0
# if(level==1):
#     smsprice = 0
#     mmsprice = (mms-50)*20
# elif(level==2):
#     smsprice = (sms-100)*10
#     mmsprice = (mms-10)*20
# elif(level==3):
#     smsprice = (sms-10)*10
#     mmsprice = (mms - 5) * 20
#
# print(f'smsPrice: {smsprice}원')
# print(f'mmsPrice: {mmsprice}원')
#
# # 8 장학금 지급 조회 7:08-19     11분
# print("\n[문제 8]")
# sem = int(input("현재까지 이수한 학기 입력  "))
# fcnt, scnt, tcnt = 0,0,0
# if (sem <= 1):
#     print("장학금 지급대상이 아닙니다.")
# else:
#     for i in range(0, sem, 1):
#         n = int(input(f"{i+1}번째 학기 이수 학점을 입력하세요."))
#         if(n<=15):
#             print("장학금 지급대상이 아닙니다.")
#             continue
#         score = float(input(f"{i+1}번째 이수 평점을 입력하세요."))
#         if(score >= 4.0):
#             print("전액 장학금!")
#             fcnt+=1
#         elif(score >=3.5):
#             print("50%장학금")
#             scnt+=1
#         elif(score>=3.0):
#             print("30%장학금")
#             tcnt+=1
#         else:
#             print("장학금 지급 대상이 아닙니다.")
#
# print("=============")
# print("현재까지장학금횟수")
# print(f'전액장학금 {fcnt}회')
# print(f'50%장학금 {scnt}회')
# print(f'30%장학금 {tcnt}회')
# print("=============")
#
# # 9 다이아몬드 출력 7:20-24         4분
# print("\n[문제 9]")
# n=5
# for i in range(n):
#     for k in range(0, n-i-1, 1):
#         print(" ", end='')
#     for j in range(0, (i+1)*2-1, 1):
#         print("*", end='')
#     print()
# for i in range(n-1):
#     for j in range(0, i+1, 1):
#         print(" ", end='')
#     for k in range(0, (n-i)*2-3, 1):
#         print("*", end='')
#     print()
#
# # 문제 10 숫자 피라미드 7:24-28      4분
# print("\n[문제 10]")
# n=int(input("숫자 피라미드의 높이 입력 : "))
# cnt=1
# for i in range(n):
#     for j in range(0, n-i-1, 1):
#         print(" ", end='')
#     for k in range(0, i+1, 1):
#         print(cnt, end=' ')
#         cnt+=1
#     print()
#
# # 문제 11  비밀번호 생성 7:45- 50          5분
# print("\n[문제 11]")
# cnt=0
# flag=False
# while(True):
#     pw=input("비밀번호 입력")
#     cnt += 1
#     if(len(pw) <6):
#         print("비밀번호의 길이가 짧습니다.")
#         continue
#     if(('!' or '@') in pw):
#         print("올바른 암호입니다.")
#         flag = True
#     else:
#         print("특수문자!or @는 포함되어야합니다.")
#         continue
#     if flag:
#         break
# print(f"귀하의 비밀번호는{pw}이며 시도한 횟수는 {cnt}입니다.")
#
# # 문제 12 숫자 맞히기 게임 7:50-8          10분
# print("\n[문제 12]")
# input("1-100중 숫자하나 생각하세요. 끝났으면 엔터 입력")
# low=1
# high=100
# cnt=1
# n=''
# while(True):
#     mid=int((low+high)/2)
#     # input에 int 씌우는거 주의하자
#     n=int(input(f"당신이 입력한 숫자는 {mid}입니다. 1.ok, 2up 3down "))
#     if(n==1):
#         break
#     elif(n==2):
#         low = mid+1
#         cnt+=1
#     elif(n==3):
#         high = mid-1
#         cnt+=1
# print(f'{cnt}회만에 찾았습니다.')
