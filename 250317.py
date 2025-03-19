'''
pi = 3.14159265
radius = int(input('원의반지름: '))
area = pi * radius * radius
print(f'원의넓이 : {area:.3f}')
'''

# 동전 교환 프로그램
# 사용자에게 금액을 입력받아 500 100 50 10의 동적으로 교환해라
'''
money = int(input('교환할 돈을 입력하세요. '))
fh = money // 500
money = money-(fh*500)
print("500원 개수 : %d개"% fh)
oh = money // 100
money = money-(oh*100)
print("100원 개수 : %d개"% oh)
ft = money // 50
money = money-(ft*50)
print("50원 개수 : %d개"% ft)
t = money // 10
money = money-(t*10)
print("10원 개수 : %d개"% t)
print("잔돈 : %d원"% money)
'''

# 가장 큰 단위부터 계산해야 한다.
money = int(input('교환할 돈을 입력하세요. '))
fh = money // 500
money = money % 500 # 잔돈 구하기.나머지 구하기. 나눈 나머지와 뺀 것과 동일하다.
# 500으로 나누고 남은 나머지 == 500을 제하고 남은 돈
print("500원 개수 : %d개" % fh)
oh = money // 100
money = money % 100
print("100원 개수 : %d개" % oh)
ft = money // 50
money = money % 50
print("50원 개수 : %d개" % ft)
t = money // 10
money = money % 10
print("10원 개수 : %d개" % t)
print("잔돈 : %d원" % money)