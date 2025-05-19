## 할인율 적용 프로그램
import module_discount as md
prod = []

while (True):
    sel = int(input("상품 구매 하시겠습니까? 1.구매 2.종료 "))
    if sel == 1:
        # 구매
        prod = md.buy(prod)
    else:
        break
# 할인율 구하기
rate = md.dccount(len(prod))
print(f"할인율 : \t{rate}%")
# 할인가 총합 구하기
sum = md.applydc(rate, prod)
print(f"총합계 : \t{sum}원")
