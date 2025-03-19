str = "반가워요"
num=10
num2=3.14
print (num, num2, 999, "hello wold!", "nice to meet you", end=' ') # ''면 공백이 없어짐.
print (str)
print ("%d" % 123.45)
print ("%f" % 123.45)
print ("%s" % 'hello')
print ("%.1f" % 123.456789) # 자동 반올림 된다. 소수점 1개까지 출력하라는 뜻
print ("%.3f" % 123.456789)

# 포맷 문자열
name = '홍길동'
age = 20
print (f'이름은 {name}이고 나이는{age}입니다.') # 자료형이 달라도 한 문장에 출력하도록 한다.

# print("%d" % (100, 200)) # TypeError 발생
# print("%d %d" %(100)) # TypeError 발생

print("내 나이는 %d 살이고, 학번은 %d 입니다.",20) # 하나만 있는 경우 콤마로만 해도 된다.
#내 나이는 %d 살이고, 학번은 %d 입니다. 20

print("내 나이는 %d 살이고, 학번은 %d 입니다." % (20, 202111))