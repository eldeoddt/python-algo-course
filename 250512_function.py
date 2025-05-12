# 계산기 프로그램
def add(n1, n2):
    return n1 + n2
def sub(n1, n2):
    return n1 - n2
def mul(n1, n2):
    return n1 * n2
def div(n1, n2):
    return n1 / n2
def calculator (n1, n2, sel):
    if sel==1:
        print(f"덧셈 결과 : {add(n1, n2)}")
    elif sel == 2:
        print(f"뺄셈 결과 : {sub(n1, n2)}")
    elif sel == 3:
        print(f"곱셈 결과 : {mul(n1, n2)}")
    elif sel == 4:
        print(f"나눗셈 결과 : {div(n1, n2)}")

n1 = int(input("숫자를 입력하세요. "))
sel = int(input("연산자 선택. 1.덧셈 2.뺄셈 3.곱셈 4.나놋셈 "))
n2 = int(input("숫자를 입력하세요. "))
calculator(n1, n2, sel)