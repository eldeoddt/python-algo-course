# 문제 1 배수 더하기
# 1~100 정수 중 4 배수이면서 6의 배우는 아닌 수의 합을 구하시오.
# 단 24의 배수는 예외로 하여 무조건 제외..

# print("[문제 1]")
# sum=0
# for i in range(1, 101, 1):
#     if((i!=24) & (i%4==0) & (i%6!=0)):
#         sum+=i
# print("합 : ", sum)

# 문제 2 소수 구하기
# 사용자로부터 정수 입력 받아, 그 수가 소수인지 판별.
# 소수? 라는 거에서 막힘.
# 교수님 풀이
# 2,3,5,7,9,11,13 등.  홀수아닌가?
# 5는 소수.
# 해당 숫자만큼 반복 돌림.1부터 나머지가 0인지 체크.
# 5의 경우 1.2.3.4.5 중 1,5일때만 나머지가 0이다.

# print("\n[문제 2]")
# num = int(input("정수를 입력하세요: "))
# if(num < 1):
#     print("1보다 큰 수를 입력하세요.")
#
# # 소수 판별 : 1과 자기 자신으로만 나눠지는 수.
# isReal = True
# for i in range(2, num, 1):
#     # print(f"num({num}) % i({i}): {num%i}")
#     if(num%i==0):
#         isReal = False
#         break
# if(isReal):
#     print("%d 은 소수입니다." % num)
# else:
#     print("%d 은 소수가 아닙니다." % num)


# 문제 3  2또는 3의 배수.
# 사용자에게 양의 수 n 입력합다, n이하 숫자 중 2 또는 3의 배수인 수만 출력하고
# 그 수의 총합을 구해라.

# print("\n[문제 3]")
# sum = 0
# n = int(input("양의 정수를 입력하세요: "))
# print("조건에 맞는 수:")
# for i in range(1, n+1, 1):
#     if((i%2==0) | (i%3==0)):
#         print(i, end=' ')
#         sum+=i
# print()
# print("합계: ", sum)

# 문제 4 조건의 수 구하기
# 양의 정수 1  부터 모든 홀수와 3의 배수 중 짝수를 더해서 나간다
# 어느 숫자까지 더해야 1000을 넘어서는지 구해라

# print("\n[문제 4]")
# num = 1
# sum = 0
# while(True):
#     if((num%2!=0) | ((num%3==0) & (num%2==0))):
#         sum+=num
#     if(sum > 1000):
#         break
#     num += 1
#
# print("1000을 넘는 숫자 ", num)
# print("그때까지의 합 ", sum)


# 문제 5 자릿수의 합 구하기
# 사용자에게 숫자 입력받아 각 자리수의 합을 구한다.
# print("\n[문제 5]")

# lenth=0
# num=" "
# intNum=0
# num=input("정수: ")
# lenth = len(num)
# intNum = int(num)
# before = 0
# sum = 0
# 100 자리는 100으로 나눈 몫이다.
# 10 자리는 100자리를 빼고 10으로 나눈 몫이다.
# 일의 자리는 10으로 나눈 나머지로 구한다.

# 자리수 고려 안하고 풀이
# one = intNum // 100
# two = (intNum // 10) % 10
# three = intNum % 10
# print("합: ", one+two+three)

# for i in range (lenth-1, 0, -1):
#     # lenth가 4인 경우
#     # len-1번. 3,2,1번 10을 곱해야 한다.
#     # 4 -> 1*10*10*10 -> 3번. **len-1**번 10을 곱해야 함
#     # 3 -> (1*10*10) 으로 나눈 몫. 1234를 100으로 나눈몫 -> 12. 근데 이 몫 구하기 전에.
#     # 이전 자리수 부분을 빼주면. 1000을빼면 234. 234를 100으로 나눈몫은 2이다.
#     # 따라서 로직을 len-1번 하고 처음/끝 아닌경우 중간인경우는 이전 자리수를 빼줘야 한다.
#     # 2 -> (1*10) % 10 -> 10 한번 곱하고, 중간 숫자들은 10으로 나눈 몫에다가 10으로 나눈 나머지 구해야 한다.?
#     # 1 -> 일의자리는 10으로 나눈 나머지만 구하면 된다.
#     print(f"i: {i}")
#     if (i==lenth-1) : # 가장 큰 자리수일 경우
#         div = 1
#         for j in range(i):  # 자리수 만들기
#             div *= 10
#             print(f"가장큰자리입니다. div: {div}")
#         max = intNum // div
#         before=max
#         sum+=max
#         print(f"max: {max}")
#
#     if (i==1) : # 일의자리수일 경우
#         print(f"일의자리입니다.")
#         one = intNum % 10
#         sum+=one
#         print(f"one:{one}")
#     else:
#         # 이전 자리수를 빼줘야 한다.
#         div=1
#         for j in range(i-1): # 자리수 만들기
#             div*=10
#             print(f"중간자리입니다. div: {div}")
#         print(f"before: {before}")
#         midNum = intNum - (div*10*before) # 수에서 이전 자리수를뺀값.
#         print(f"midNum: {midNum}")
#         #몫을 구하기
#         mid=midNum//div
#         print(f"mid:{mid}")
#         before=mid
#         sum+=mid
#     print(f"sum: {sum}")

# 문자열 배열을 사용한 방법.. 짧다.
# for i in num:
#     sum+=int(i)
# print(sum)


# 문제 6 온도
# 사용자로부터 초기 온도, 목표 온도 입력
# 매 반복마다 온도를 10%씩 감소한다.
# 몇 번만에 목표 온도 이하로 떨어지는지 구해라

# print("\n[문제 6]")
# cnt = 0
# temp = int(input("초기 온도를 입력하세요: "))
# target = int(input("목표 온도를 입력하세요: "))
# while(True):
#     temp -= (temp * 0.1)
#     cnt+=1
#     if(target >= temp):
#         print(f"{cnt}회 후 온도는 {temp:.6f}도이며 목표에 도달합니다.")
#         break

# f-string에서 소수점 개수를 조절하는 방법 : {temp:.6f}
# 10%감소 구현 시 10%를 적용하는 것이 아니라 원래 수에서 빼줘야 하는 것에 주의한다..
# 10%를 적용해버렸다.

# 문제 7 문자 메시지 요금 계산하기
# print("\n[문제 7]")
# print("회원 등급을 선택하세요.")
# level = int(input("1.VVIP   2.VIP   3.GOLD "))
# sms = int(input("SMS 발송 건수를 입력하세요. "))
# mms = int(input("MMS 발송 건수를 입력하세요. "))
# mmsPrice = 0
# smsPrice = 0
# # 계산
# if (level == 1):
#     if(mms > 50):
#         mmsPrice = (mms-50)*20
# elif (level == 2):
#     if(sms > 100):
#         smsPrice = (sms-100)*10
#     if(mms > 10):
#         mmsPrice = (mms-10)*20
# elif (level == 3):
#     if(sms > 10):
#         smsPrice = (sms-10)*10
#     if(mms > 5):
#         mmsPrice = (mms-5)*20
# else: print("1-3사이 값을 입력하세요.")
#
# print(f"smsPrice : {smsPrice}원")
# print(f"mmsPrice : {mmsPrice}원")

# 예외 처리를 해볼 수 있겠다.

# 문제 8 장학금 지급 조회
# 1학기 수료, 8학기 넘으면 안됨, 한 학기 이수 학점이 15보다 낮으면 안됨.
# 4 이상이면 전액
# 3.5 이상 - 50%
# 3 이상 - 30%
# 3안되면 받을 수 없다.
# print("\n[문제 8]")
# scholar = [0,0,0]
# sem = int(input("현재까지 이수한 학기를 입력하세요. "))
# if((sem<=1) | (sem>7)):
#     print("장학금 지급 대상이 아닙니다.")
# else:
#     for i in range(sem):
#         credit = int(input(f"{i+1}번째 학기 이수 학점을 입력하세요. "))
#         if (credit <= 15):
#             print("장학금 대상이 아닙니다.")
#             continue
#
#         avg = float(input(f"{i+1}번째 학기 이수 평점을 입력하세요. "))
#
#         if (avg>=4):
#             print("전액 장학금!")
#             scholar[0]+=1
#         elif (avg>=3.5):
#             print("50% 장학금!")
#             scholar[1] += 1
#         elif (avg>=3):
#             print("30% 장학금!")
#             scholar[2] += 1
#         else:
#             print("장학금 대상이 아닙니다.")
#     print("===================")
#     print("현재까지 장학금 횟수")
#     print(f"전액 장학금 {scholar[0]}회\n50% 장학금 {scholar[1]}회\n30% 장학금 {scholar[2]}회")
#     print("===================")
# continue를 사용하면 아래를 생략하고 다시 조건 비교하는 곳을 이동한다.

# 문제 9 다이아몬드 출력
# print("\n[문제 9]")
# n=10
# m=7
# for i in range(1, n, 2):
#     # 공백
#     for j in range(int((n-i)/2), 0, -1):
#         print(" ", end='')
#     # *
#     for k in range(i):
#         print("*", end='')
#     print()
# for i in range(m, 0, -2):
#     # 공백
#     for j in range(0, int((n-i)/2), 1):
#         print(" ", end='')
#     # *
#     for k in range(i):
#         print("*", end='')
#     print()
# i를 사용해야 매 반복 마다 숫자가 i에 따라 동적으로 바뀐다.
# -> i를 잘 사용해야 한다.

# 문제 10 숫자 피라미드
# 사용자로부터 양의 정수 n 입력, 1부터 숫자 증가시키며 피라미드 출력.
# print("\n[문제 10]")
# num = int(input("숫자 피라미드의 높이를 입력하세요: "))
# cnt=1
# for i in range(0, num ,1):
#     # 공백
#     for j in range((num-i-1), 0, -1):
#         print(" ", end='')
#
#     # 숫자
#     for k in range(0, i+1, 1):
#         print(cnt, end=' ')
#         cnt+=1
#     print()
# 30분 넘게 걸린 것 같다.. 숫자가 증가하는 부분을 반복문으로 생각하니 전혀 알수가 없었다.
# 그래서 초심으로 별부터 하나씩 증가시키며 찍어보았다.
# 생각해보니 그냥 전역변수 숫자를 하나씩 증가시키는 것이 맞는 것 같았다.
# 너무 어렵게 생각 했다. 다른 증가 값이 있어도 별부터 찍어 보자.

# 문제 11 비밀번호 생성
print("\n[문제 11]")
cnt=0
special = False
while(True):
    str = input("비밀 번호를 입력하세요 ")
    cnt += 1
    if(len(str)<6):
        print("비밀번호의 길이가 짧습니다.")
        continue
    for i in str:
        if(i in ["!", "@"]):
            special = True
            break
    if(special == True): break
    print("특수문자(! 또는 @) 포함되어야 합니다.")

print("올바른 암호 입니다.")
print(f"귀하의 비밀번호는 {str} 이며 시도한 횟수는 {cnt} 입니다.")

# break로 while을  빠져나오고 싶었는데, for만 빠져나와서 flag변수를 추가해서 명시적으로 while을 탈출하도록 했다.
# continue로 길이를 먼저 체크하고 다시 입력을 받는다.
# 입력을 받을 때마다 count를 증가시켰다.아래쪽에 두면 집계가 안되기 때문에.
# while 사용 시에는 if로 명시적으로 탈출하자.

# 문제 12 숫자 맞히기 게임
# 2진 탐색 알고리즘 사용
# print("\n[문제 12]")
# low = 1
# high = 100
# cnt = 0
# input("1-100 중 숫자 하나를 생각하세요. 생각이 끝났으면 Enter를 입력합니다.")
# while(True):
#     mid = (low + high)/2
#     select=int(input(f"당신이 입력한 숫자는 {mid:.0f}입니다. 1.OK, 2.UP, 3.DOWN "))
#     if(select == 1):break
#     if(select == 2):
#         low=mid
#         mid+=(high-mid)/2
#         cnt += 1
#         continue
#     if(select == 3):
#         high=mid
#         mid -= (mid-low) / 2
#         cnt += 1
#         continue
# print(f"{cnt}회 만에 찾았습니다.")
# 재미있었다.
# 자료구조 수업에서 완벽하게 숙지하지 못했지만 손이 기억한 것 같다..
# 논리적으로 머릿속에 그려가며 풀었는데
# 한번만에 내 생각대로 탐색되어서 신기했다.
# 이진 탐색의 기본 개념을 그대로 적용했다. 계속 반으로 나누어 가며
# up이면 현재 mid를 low로 놓고, down이면 현재 mid를 high로 놓는다.
# 그리고 mid 계산은 입력 전에 수행한다. 사용자 입력에 따라 low/high를 재설정 하는 것이라서
# count는 low/high를 바꾼 경우에만 증가시켰다.