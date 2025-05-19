## 할인된 상품 가격표
prod = {"쌀":9900, "상추":1900, "고추":2900, "마늘":8900, "통닭":5600, "햄":6900, "치즈":3900}
dcprod = {}

def dc(rate) :
    for i in prod.keys():
        dcprod[i] = int(prod[i] - (prod[i]*rate/100))
    pr(rate)
def pr(rate) :
    for i in prod.keys():
        print(f"{i}\t : {prod[i]}원 {rate} %DC -> {dcprod[i]} 원")

rate = int(input("오늘의 할인율 "))
dc(rate)


