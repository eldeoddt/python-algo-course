# *가 트리 모양으로 출력될 수 있도록 하시오. 2:57-3:00        3분
n = 6
for i in range(0, n, 1):
    # space
    for k in range(n - i - 1, 0, -1):
        print(" ", end='')
    # star
    for j in range(0, (i + 1) * 2 - 1, 1):
        print("*", end='')
    print()

# * 가 트리 모양, 숫자 증가하시오. 3:06-3:09       3분
n = 6
cnt = 1
for i in range(0, n, 1):
    # space
    for k in range(n - i - 1, 0, -1):
        print(" ", end='')
    # star
    for j in range(0, i + 1, 1):
        print(f"{cnt}", end=' ')
        cnt += 1
    print()

# 다이아몬드 숫자 출력하기. 3:11-3:17              6분
n = 4
m = 3
cnt = 1
for i in range(0, n, 1):
    # space
    for k in range(n - i - 1, 0, -1):
        print(" ", end='')
    # number
    for j in range(0, i + 1, 1):
        print(f"{cnt}", end=' ')
        cnt += 1
    print()
i, j, k, cnt = 0, 0, 0, 6
for i in range(0, m, 1):
    # space
    for k in range(0, i + 1, 1):
        print(" ", end='')
    # number
    for j in range(m - i, 0, -1):
        print(f"{cnt}", end=' ')
        cnt -= 1
    print()
n = 4
m = 3
cnt = 1
for i in range(0, n, 1):
    # space
    for k in range(n - i - 1, 0, -1):
        print(" ", end='')
    # number
    for j in range(0, i + 1, 1):
        print(f"{cnt}", end=' ')
        cnt += 1
    print()

# 다이아몬드 숫자 출력 응용1 . 3:21- 25              4분
n = 4
m = 3
cnt = 1
for i in range(0, n, 1):
    # space
    for k in range(n - i - 1, 0, -1):
        print(" ", end='')
    # number
    for j in range(0, i + 1, 1):
        print(f"{cnt}", end=' ')
        cnt += 1
    print()
i, j, k, cnt = 0, 0, 0, 0
for i in range(0, m, 1):
    if (i == 0): cnt = 4
    if (i == 1): cnt = 2
    if (i == 2): cnt = 1
    # space
    for k in range(0, i + 1, 1):
        print(" ", end='')
    # number
    for j in range(m - i, 0, -1):
        print(f"{cnt}", end=' ')
        cnt += 1
    print()



# 별과 숫자 교차 피라미드 . 3:28 - 3:34               6분
n=5
cnt=1
for i in range(0, n, 1):
    # space
    for k in range((n-i)*2-2, 0, -1):
        print(" ", end='')
    # star and number
    for j in range(0, (i+1)*2-1, 1):
        if(j%2==0):
            print("*", end=' ')
        else:
            print(f"{cnt}", end=' ')
            cnt+=1
    print()
print()
# 2차 8:40-8:55                 15분
n=5
cnt=1
for i in range(0, n, 1):
    # space
    for k in range((n-i)*2-2, 0, -1):
        print(" ", end='')
    # star
    for j in range(0, (i+1)*2-1, 1):
        if(j%2==0): # 0부터 짝수인 경우 -> 0은 따로 처리 -> 아니 cnt로 따지는게 맞는듯 -> 아니 그럼 짝수인거만 출력되니까 j로 하는게 맞음
            print("*", end=' ')
        else:
            print(cnt, end=' ')
            cnt+=1
    print()

# 좌우 대칭 피라미드 3:37-3:43                  6분
n=5
for i in range(0, n, 1):
    # space
    for k in range((n-i)*2-2, 0, -1):
        print(" ", end='')
    # star and number
    for j in range(0, (i+1)*2-1, 1):
        # if(j==0 or j==(i+1)*2-2):
        #     print(f"{i + 1}", end=' ')
        # else:
        #     print("*", end=' ')

        if (j!=0 or j!=((i+1) *2 -2)):  # !=로는 왜 안되는지?...
            print("*", end=' ')
        else:
            print(f"{i + 1}", end=' ')
    print()

# 2차 8:56-9:01             4분
n=5
for i in range(0, n, 1):
    for j in range((n-i)*2-2, 0, -1):
        print(' ', end='')
    for k in range(0, (i+1)*2-1, 1):
        if(k == 0 or k == (i+1)*2-2):
            print(i+1, end=' ')
        else:
            print("*", end=' ')
    print()

# 역숫자 피라미드 9:06- 9:26                          20분
#n = int(input("줄 수 입력:  "))
n=5
cnt=1
for i in range(0, n, 1):

    for j in range(0, i*2, 1):
        print(" ", end='')

    if (i == 0):
        for k in range(0, 9, 1):
            print(cnt, end=' ')
            cnt += 1
        print()
        continue

    for k in range(n-i+4, 2, -1):
        print(cnt, end=' ')
        cnt+=1
    print()

# 다이아몬드 숫자 2차 00-05        5분
n=4
cnt=1
for i in range(n):
    for k in range(0, n-i-1, 1):
        print(" ", end='')
    for j in range(0, i+1, 1):
        print(cnt, end=' ')
        cnt+=1
    print()
cnt=6
for i in range(n-1):
    for j in range(0, i+1, 1):
        print(" ", end='')
    for k in range(0, n-i-1, 1):
        print(cnt, end=' ')
        cnt-=1
    print()

# 별과 숫자 교차 피라미드 2차 13-16      3분
cnt=1
n=5
for i in range(n):
    for k in range(0, n-i-1, 1):
        print(" ", end=' ')
    for j in range(0, (i+1)*2-1, 1):
        if(j%2==0): # 짝수 j이면(홀수)
            print("*", end=' ')
        else:
            print(cnt, end=' ')
            cnt+=1
    print()

