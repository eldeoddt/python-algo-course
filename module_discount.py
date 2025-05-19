def applydc(rate, prod):
    sum = 0
    for i in prod:
        sum += (i - (i * (rate / 100)))
    return sum


def dccount(len):
    dcrate = 0
    if len == 1:
        dcrate = 5
    elif len == 2:
        dcrate = 10
    elif len == 3:
        dcrate = 20
    elif len >= 4:
        dcrate = 30
    return dcrate


def buy(prod):
    price = int(input("구매한 상품의 금액을 입력하세요. "))
    prod.append(price)
    return prod