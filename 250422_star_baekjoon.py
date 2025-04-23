# 백준 별 찍기 -1 2분
n = int(input("n 입력 "))
for i in range(0, n, 1):
    for j in range(0, i+1, 1):
        print("*", end='')
    print()

# 백준 별 찍기 -2 1분
n = int(input("n 입력 "))
for i in range(0, n, 1):
    for k in range(n-i-1, 0, -1):
        print(" ", end='')
    for j in range(0, i+1, 1):
        print("*", end='')
    print()

# 백준 별 찍기 -3 1분
n = int(input("n 입력 "))
for i in range(0, n, 1):
    for k in range(n-i, 0, -1):
        print("*", end='')
    print()

# 백준 별 찍기 -4 1분
n = int(input("n 입력 "))
for i in range(0, n, 1):
    for j in range(0, i, 1):
        print(" ", end='')
    for k in range(n-i, 0, -1):
        print("*", end='')
    print()

# 백준 별 찍기 -5  5분
n = int(input("n 입력 "))
for i in range(n):
    for j in range(0, n-i-1, 1):
        print(" ", end='')
    for k in range(0, (i+1)*2-1, 1):
        print("*", end='')
    print()

# 백준 별 찍기 -6 2분
n = int(input("n 입력 "))
for i in range(n):
    for j in range(0, i, 1):
        print(" ", end='')
    for k in range(0, 2*(n-i)-1, 1):
        print("*", end='')
    print()

# 백준 별 찍기 -7  5분
n=int(input("n  "))
for i in range(n):
    for j in range(0, n-i-1, 1):
        print(" ", end='')
    for k in range(0, (i+1)*2-1, 1):
        print("*", end='')
    print()
for i in range(n-1):
    for j in range(i+1):
        print(" ", end='')
    for k in range(2*(n-i)-3):
        print("*", end='')
    print()

# 백준 별 찍기 -8  24-39    15분
n=int(input("n  "))
for i in range(n):
    for j in range(0, i+1, 1):
        print("*", end='')
    for k in range(0, (n-i)*2-2, 1):
        print(" ", end='')
    for l in range(0, i+1, 1):
        print("*", end='')
    print()

for i in range(n-1):
    for j in range(0, n-i-1, 1):
        print("*", end='')
    for k in range(0, (i+1)*2, 1):
        print(" ", end='')
    for l in range(0, n-i-1, 1):
        print("*", end='')
    print()

# 백준 별 찍기 -9 1:53 -2:01    8분
n=int(input("n  "))
for i in range(n):
    for j in range(0, i, 1):
        print(" ", end='')
    for k in range(0, (n-i)*2-1, 1):
        print("*", end='')
    print()
m=n-1
for i in range(m):
    for j in range(0, m-i-1, 1):
        print(" ", end='')
    for j in range(0, (i+1)*2+1, 1):
        print("*", end='')
    print()

# 백준 별 찍기 -10
# 재귀 패턴 N이 3의 거듭 제곱이다. 크기 N 패턴은 n*n 정사각형
# 가운데 공백, 가운데 제외한 모든 칸에 별이 하나씩 있다.


# 백준 별 찍기 -12     4분
n=int(input())
for i in range(n):
    for j in range(0, n-i-1, 1):
        print(" ", end='')
    for k in range(0, i+1, 1):
        print("*", end='')
    print()
for i in range(n-1):
    for j in range(0, i+1, 1):
        print(" ", end='')
    for k in range(0, n-i-1, 1):
        print("*", end='')
    print()
# 백준 별 찍기 -13     1분
n=5
for i in range(n):
    for j in range(0, i+1, 1):
        print("*", end='')
    print()
for i in range(n-1):
    for j in range(0, n-i-1, 1):
        print("*", end='')
    print()

# 백준 별 찍기 -15 33- 40
# 이거 중간에 print가 있어서 오타로 시간을 잡아먹음.
n=5
for i in range(n):
    for j in range(0, n-i-1, 1):
        print(" ", end='')
    for k in range(0, (i+1)*2-1, 1):
        if(k==0 or k==(i+1)*2-2):
            print("*", end='')
        else:
            print(" ", end='')
    print()

# 백준 별찍기 -16 1분
n=5
for i in range(n):
    for k in range(0, n-i-1, 1):
        print(" ", end='')
    for j in range(0, i+1, 1):
        print("*", end=' ')
    print()

# 백준 별찍기 -17 58- 06 -25     8분 -> 각 뒷줄의 공백이 있으면안된대요. 27분
n=5
for i in range(n):
    for k in range(0, n-i-1, 1): # 주의: 꼭 맨 왼쪽 공백이 있는지 확인한다.
        print(" ", end='')
    for j in range(0, (i+1)*2-1):
        if(i==0 or i==n-1):
            print("*", end='') # 주의: end 공백이 없어야 한다.
        elif(j==0 or j==(i+1)*2-1-1): # 양끝에만 출력.
            print("*", end='')
        else:
            print(" ", end='')
    print()