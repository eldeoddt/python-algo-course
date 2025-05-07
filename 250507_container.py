# 실전 예제 1 - 수학시험 프로그램 ; 튜플
pbtuple = ("3+2","5/2의 몫", "10-2", "10^2 * 2", "1-(10/4의 나머지)", "2^4", "4/2")
anstuple= (5, 2, 8, 200, -1, 16, 2)
score = (3, 5, 3, 5, 5, 3, 3)
corcnt=0
totalscore=0
for i in range(len(score)):
    print("문제 : ",pbtuple[i])
    ans = int(input("정답을 입력하세요. "))
    if anstuple[i]==ans :
        corcnt+=1
        totalscore += score[i]
print("-"*10)
print(f"정답 개수: {corcnt}")
print(f"오답 개수: {len(score)-corcnt}")
print(f"Total Score: {totalscore}")
print("-"*10)

# 교수님 풀이
quiz=(["3+2", 5, 3], ["5/2의 몫", 2, 5], ["10-2", 8, 3], ["10^2 * 2", 200, 5], ["1-(10/4의 나머지)", -1, 5], ["2^4", 16, 3], ["4/2", 2, 3])
corcnt=0
totalscore=0
for i in range(len(quiz)):
    print("문제 : ",quiz[i][0])
    ans = int(input("정답을 입력하세요. "))
    if quiz[i][1]==ans :
        corcnt+=1
        totalscore += quiz[i][2]
print("-"*10)
print(f"정답 개수: {corcnt}")
print(f"오답 개수: {len(quiz)-corcnt}")
print(f"Total Score: {totalscore}")
print("-"*10)

# 실전 예제 2 - 회원가입 프로그램 ; 딕셔너리
user={}
while(True):
    sel = int(input("1. 회원가입, 2. 프로그램 종료 "))
    if(sel==2):break
    elif(sel==1):
        id=input("아이디를 입력하세요. ")
        pw=input("비밀번호를 입력하세요. ")
        print()
        user[id] = pw

    else:
        print("1 또는 2를 입력하세요.")
        print()
print("-"*28)
print("아이디 : 비밀번호")
print("-"*28)
for i in user.keys():
    print(f"{i}\t:\t{user[i]}")
print("-"*28)