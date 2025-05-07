## 예제 2 혈액 보관 시스템
# bt=[]
# for i in range(0, 10, 1):
#     bt.append(input("혈액형 선택"))
#
# # list.count()함수 사용
# print("A형 : ", bt.count('A'))
# print("B형 : ", bt.count('B'))
# print("AB형 : ", bt.count('AB'))
# print("O형 : ", bt.count('O'))
#
# # 함수 안 쓰는 풀이
# a,b,ab,o=0,0,0,0
# for i in range(10):
#     if(bt[i]=='A'):
#         a+=1
#     elif(bt[i]=='B'):
#         b+=1
#     elif (bt[i] == 'AB'):
#         ab += 1
#     elif (bt[i] == 'O'):
#         o += 1
#
# print("A형 : ", a)
# print("B형 : ", b)
# print("AB형 : ", ab)
# print("O형 : ", o)

# # 예제 3 화학 주기율표 찾기
# symbol=["F"]
# name=["플루오린"]
#
# # list.index() 함수 사용
# sym = input("심볼 입력 ")
# id=symbol.index(sym)
# print(f"이 심볼의 이름은 {name[id]}입니다.")
#
# # 반복변수 사용
# # len()사용 안하고 정수 넣으면 out of range 발생 가능.
# for j in range(0, len(symbol), 1):
#     if symbol[j]==sym:
#         print(f"이 심볼의 이름은 {name[j]}입니다.")

# dictionary
score={"c/c++":"A","Java":"B+","Mobile":"C","Security":"A+"}
print(score)
print(score["Java"], score["Security"])
score["python"]="A"
score["OS"]="A+"
print(score)
score["Java"]="F"
score["System"]="A"
print(score)

# 값 순으로 정렬 하고 싶음..
sorted(score.items())
print(score)
for i in score.keys(): # 전체 키들을 반환한다.
    print(i, score[i])