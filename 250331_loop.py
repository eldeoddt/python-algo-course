## 반복문
# p16. -2
min = 0
cnt = 0
for i in range(1,101,1):
    if((i%3==0) & (i%7==0)):
        print("3과 7의 공배수: ",i)

        if(min == 0): # min == 0이면 min에 i대입.
            # -> 가장 처음 if를 만족하는 값을 저장해야 함.
            # 가장 처음 만족. if에 들어간다면. min 가장 처음에만 저장.
            min = i

        cnt += 1
        if (cnt == 1):  # min == 0이면 min에 i대입.
            # -> 가장 처음 if를 만족하는 값을 저장해야 함.
            # 차라라 count를 세는건 어떤가?
            min = i
print("3과 7의 최소공배수: ",min)

# len(str1)
str1 = 'hello'
for c in range(0, len(str1), 1):
    print (str1[c])

# 홀짝 구분 p31
num = 1
while(num <= 30):
    if(num%2 ==0):
        print("짝수 : " , num)
    else:
        print("홀수 : ", num)
    num +=1

# 100까지 정수 중 3, 8의 공배수와 최소공배수 출력
min = 0
num = 1
while(num <=100) :
    if ((num%3==0) & (num%8==0)):
        print("공배수 : ", num)

        if(min==0):
            min = num
    num += 1
print("최소공배수 : ", min)