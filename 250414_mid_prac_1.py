# 4문제. 3문제는 이런 난이도 1문제는 어렵.
# 결과창 일부 다르면 부분 점수.
# 효율은 안따짐. 잘 돌아가면 된다.

# 다시 풀어보기
# # 문제 7 3:11 - 3:18
print("\n[문제 7]")
print("회원 등급을 선택하세요.")
lev = int(input("1vvip, 2vip 3gold"))
sms = int(input("sms건수"))
mms = int(input("mms건수"))
mmsp = 0
if (lev == 1):
    # 50까지 무제한, 51건부터 1건당 20원
    sms = 0
    if (mms > 50):
        mmsp = (mms - 50) * 20
elif (lev == 2):
    if (sms > 100):
        sms = (sms - 100) * 10
    if (mms > 10):
        mms = (mms - 10) * 20
elif (lev == 3):
    if (sms > 10):
        sms = (sms - 10) * 10
    if (mms > 5):
        mms = (mms - 5) * 20
print("sms: ", sms)
print("mms: ", mmsp)

# 문제 8
# 3:19 - 3:29
print("\n[문제 8]")
allcount = 0
fcount = 0
tcount = 0
sem = int(input("현재까지 이수한 학기 입력 "))
if ((sem <= 1) | (sem > 7)):
    print("장학금 지급 대상이 아닙니다.")
for i in range(1, sem + 1, 1):
    score = float(input(f"{i}번째 이수 학점 입력 "))
    if (score <= 15):
        print("장학금 지급 대상이 아닙니다.")
        continue
    avg = float(input(f"{i}번째 이수 평점 입력 "))

    if (avg >= 4):
        print("전액장학금")
        allcount += 1
    elif (avg >= 3.5):
        print("50%장학금")
        fcount += 1
    elif (avg >= 3.0):
        print("30%장학금")
        tcount += 1
    else:
        print("장학금 지급 대상이 아닙니다.")
print("=============")
print("현재까지장학금횟수")
print("전액", allcount)
print("50", fcount)
print("30", tcount)
print("=============")

# 문제 9
# 3:32 - 4:8
print("\n[문제 9]")
n=10
for i in range(1, n, 2):
    # 공백
    for k in range(int((n-i)/2), 0, -1):
        print(" ", end='')

    # 별
    for j in range(0, i, 1):
        print('*', end='')
    print()

m=8
for i in range(m, 0, -2):
    # 공백
    for k in range(int((m-i)/2)+1, 0, -1):
        print(" ", end='')

    # 별
    for j in range(0, i-1, 1):
        print('*', end='')
    print()
# 어렵다.. 각자 따로 공백 따로 별 따로 찍어봐야 한다.

# 문제 10
# -
print("\n[문제 10]")

# 문제 11
# -
print("\n[문제 11]")

# 문제 12
# -
print("\n[문제 12]")