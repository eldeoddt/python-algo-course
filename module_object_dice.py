import random as rd
# 랜덤 생성 함수
def generateNum():
    num=[]
    for i in range(5):
        rdn = rd.randint(1, 6)
        num.append(rdn)
    return num