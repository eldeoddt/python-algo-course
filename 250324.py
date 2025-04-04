# 반복문, 조건문 잘 쓰는 것이 중요.
# 결과를 보고 코드 작성하는 방식으로 시험 출제함.

# 5-5 BMI 지수 입력받기
'''
bmi = int(input('BMI 지수를 입력하세요. '))

if (bmi>140): #140 초과
    print('고도 비만')
elif (bmi>120): #120 초과
    print('비만')
elif (bmi>110): #110 초과
    print('과체중')
elif (bmi>90): #90 초과
    print('정상 체중')
    # 그냥 else로 해도 되지 않나?
elif (bmi<=90): # 90 이하
    print('저체중')
'''

# 5-6 버스 단속 프로그램
# 버스 전용차로에 버스가 아닌 승용차가 주행할 경우 단속.
# 토요일, 공휴일은 단속하지 않음.
print("1. 월~금, 2. 토요일, 3. 공휴일")
date = int(input("요일을 선택하세요. "))

# 해야될 것이 가장 작은 것. 일반적인 것부터 먼저 처리한다.

if (date == (2 or 3) & (date < 4) & (date > 0)):
    print("토요일 및 공휴일은 단속하지 않습니다.")
elif (date == 1):
    print("버스 전용차로 단속 중입니다.")
    print("1. 버스, 2. 승용차")
    car = int(input("차종을 선택하세요. "))
    if(car == 1):
        print("버스입니다.")
    elif(car == 2):
        print("버스 전용차로 위반!!")
    else:
        print("1~2 사이의 값을 입력하세요.")
else:
    print("1~3 사이의 값을 입력하세요.")