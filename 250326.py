# 고농도 미세먼지 비상저감조치를 위한 차량 2부제 프로그램.
print("====== 차량 2부제 프로그램 ======")
import datetime

num = int(input("차량 번호 4자리를 입력하세요. "))

now = datetime.datetime.now()
date = int(now.strftime("%d"))
print("오늘 날짜 : %d일" % date)
# 출력
print("오늘 입차 : ", end="")
if((date%2)==0) :
    isEven = True
    print("번호가 짝수인 차량")
    if((num%2) != 0) : #차 번호가 홀수인 경우
        print("귀하의 차량은 입차 불가합니다.")
    else:
        print("귀하의 차량은 입차 가능합니다.")
else:
    isEven = False
    print("번호가 홀수인 차량")
    if ((num % 2) == 0):  # 차 번호가 짝수인 경우
        print("귀하의 차량은 입차 불가합니다.")
    else:
        print("귀하의 차량은 입차 가능합니다.")
        

# 생존율 출력
# 장비를 사용하기까지 걸린 시간을 입력하면 생존율이 출력되는 프로그램
print("====== 생존율 출력 프로그램 ======")
time = int(input("최초 장비를 사용하기까지 걸린 시간(초)를 입력하세요. "))
if(time < 60):
    servive = "85%"
elif(time <= 120):
    servive = "76%"
elif(time <= 180):
    servive = "66%"
elif(time <= 240):
    servive = "57%"
elif(time <= 300):
    servive = "47%"
else:
    servive = "25% 미만"

print("생존율 : ", servive)

# 전기 요금 계산기
# 전기 많이 쓰면 누진세가 붙어 단가와 기본요금이 올라감.
# 사용량 입력 -> 전기료 출력
print("====== 전기 요금 계산기 ======")
use = float(input("전기 사용량을 입력하세요. "))
if (use < 200):
    originfee = 910
    fee = 99.3
elif (use < 400):
    originfee = 1600
    fee = 186.9
else :
    originfee = 7300
    fee = 280.6

print("사용량 : %.1f kwh" % use)
print("기본요금 : %.1f원" % originfee)
print("단가 : %.1f원" % fee)
print("전기 요금 : %.1f원" % (originfee + (fee*use)))

# Bmi 계산기
print("====== BMI 계산기 ======")
name = input("이름 입력 : ")
height = int(input("키 입력 : "))
weight = int(input("몸무게(kg) 입력 : "))

bmi = (weight / ((height/100)*(height/100)))
# bmi 계산식 실수함. 코드 실수 아님.
if (bmi<18.5):
    state = "저체중"
elif (bmi<23):
    state = "정상"
elif (bmi<25):
    state = "과체중"
elif (bmi<30):
    state = "비만"
else:
    state = "고도비만"

print("%s님의 키는 %d cm 이고 몸무게는 %d kg 입니다." % (name, height, weight))
print("BMI 지수는 %.2f 입니다. %s 입니다." % (bmi, state))

# 윤년
print("====== 윤년 계산기 ======")
year = int(input("연도를 입력하세요. "))
# 연돠 4로 나누어 떨어지면서
# 100의 배수 연도가 아닐 때 또는 400의 배수일 때.
if( ((year % 4) == 0) & (((year % 100) != 0) or ((year % 400) == 0) ) ):
    print("%d 년은 윤년입니다." % year)
else:
    print("%d 년은 윤년이 아닙니다." % year)