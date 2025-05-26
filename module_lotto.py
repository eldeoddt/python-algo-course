# 사용자 번호 입력
def my_num():
    print("1-45 정수 6개 입력")
    num = []
    # 사용자에게 로또 번호 입력받기
    for i in range(6):
        n = int(input(f"Number {i+1} : "))
        num.append(n)
    return num

# 로또번호 생성
def lotto ():
    import random
    # 랜덤 숫자 6개 생성.
    lt = random.sample(range(1, 46), 6)
    return lt

# 내번호 하나씩 로또번호 리스트와 대조한다.
def verify (lt, numlist):
    result=[]
    for i in numlist:
        for j in lt:
# numlist[0]일때 lt의 모든 값과 비교하여
# 같으면 numlist[0]을 append한다.
            if i==j:
                result.append(i)
    return result