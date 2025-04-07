# 실전 예제 1 - 369 게임 만들기. 99까지아니라 1000까지 해보기
for i in range(1, 100, 1):
    if(i<=9) :
        print(i, end="")
        # 3의 배수
        if(i%3 == 0):
            print(" 짝!", end="")
        print()
    else :
        print(i, end=" ")
        # 10~99는 따로 처리한다.
        firstNum = i // 10
        secondNum = i % 10
        if firstNum % 3 ==0 :
            print(" 짝!", end="")
        elif (secondNum % 3 == 0) and (secondNum!=0):
            print(" 짝!", end="")
        print()


print("짝!")


# 실전 예제 2 - 열차 교차 시간 알아내기
# 3개 노선 열차가 9-6 운행
# a:10 , b: 25, c: 30
# 10 20 30 40 50 60
# 25 50
# 30 60 -> 공배수 구하기
# 9-6 은 540분.
# for i in range (1, 541, 1):
#     if ( ((i%10==0) & (i%25==0))
#     | ((i%25==0) & (i%30==0))
#     | ((i%10==0) & (i%30==0))
#     ):
#         print("%d시 %d분" % ((i//60)+9, i%60))

# 실전 예제 3 - 로그인 기능 만들기
# 관리자가 암호 입력, 로그인 시도 할 때 암호 틀린경우. 암호 다시 확인하세요 출력
# 5회 이상 -> 메시지 추력 종료
realpw = "hanbitac"
cnt = 0

# # 교수님 풀이
# while (True):
#     pw = input("관리자 암호를 입력하세요. ")
#     cnt +=1
#     if (cnt >= 5):
#         print("로그인 실패!! 횟수 초과!!!")
#         break
#     else :
#         if (pw == realpw):
#             print("로그인 됐습니다.")
#             break
#         else :
#             print("암호를 다시 확인하세요!")
# # 내 풀이
# while (True):
#     pw = input("관리자 암호를 입력하세요. ")
#     cnt +=1
#     if (pw == realpw) :
#         print("로그인 됐습니다.")
#         break
#     elif (cnt >= 5):
#         print("로그인 실패!! 횟수 초과!!!")
#         break
#     else :
#         cnt+=1
#         print("암호를 다시 확인하세요!")

# 실전 예제 4 - 대회 평가 점수 구하기

# 최고 점수 중복  카운트하기
# score=[0, 0, 0,0,0, 0]
# max = 0
# sum=0
#
# for i in range(1, 6, 1):
#     score[i] = int(input("심사위원%d 평가 점수: " % i))
#     # 최고 점수 구하기
#     if(max <= score[i]) :
#         max = score[i]
#         maxIndex = i
#     print(score)
#     print("max ", max)
#     print("maxindex: ", maxIndex)
# # 작품 평가 점수: 심사위원 평가 점수 중 최고 를 뺀 나머지 점수들의 평균.
# cntRemain = 0
# for i in range (1, 6, 1):
#     if(score[i]!=max):
#         print("score[i]!=max", score[i])
#         sum+=score[i]
#         cntRemain += 1
#
#     print("sum ; ", sum)
# sum = sum / cntRemain
#
# print("작품 평가 점수: ", sum)


# score=[0, 0, 0,0,0, 0]
# max = 0
# sum=0
#
# for i in range(1, 6, 1):
#     score[i] = int(input("심사위원%d 평가 점수: " % i))
#     # 최고 점수 구하기
#     if(max <= score[i]) :
#         max = score[i]
#         maxIndex = i
#     print(score)
#     print("max ", max)
#     print("maxindex: ", maxIndex)
# # 작품 평가 점수: 심사위원 평가 점수 중 최고 를 뺀 나머지 점수들의 평균.
# cntRemain = 4
# for i in range (1, 6, 1):
#     if(i!=maxIndex):
#         print("score[i]!=max", score[i])
#         sum+=score[i]
#     print("sum ; ", sum)
#
# sum = sum / cntRemain
# print("작품 평가 점수: ", sum)

# 교수님풀이
# score=[0, 0, 0,0,0, 0]
# max = 0
# sum = 0
#
# for i in range(1, 6, 1):
#     score[i] = int(input("심사위원%d 평가 점수: " % i))
#     # 최고 점수 구하기
#     if(max <= score[i]) :
#         max = score[i]
#     sum+=score[i] # 모두 더하기
# print("작품 평가 점수: ", (sum-max)/4)

# 실전 예제 5 - 심박수 구하기
level = [40, 50, 60, 70, 80]
age = int(input("나이: "))
relax = int(input("안정 시 심박수: "))
for i in range(0, 5, 1):
    # 40%이므로 40 / 100으로 정확 하게!!!!! 해야 한다.
    # i 로 썻다가 틀림.. level i 로 써야한다.
    point = ( ( (220 - age) - relax ) * (level[i]*0.01) ) + relax
    print("강도: %d%% 목표 심박수: %.1fbpm" % (level[i], point))

# 교수님풀이
# for i in range(40, 90, 10):