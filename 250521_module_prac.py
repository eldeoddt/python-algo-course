# 모듈 사용하기
# 로 또 당첨 게임
import module_lotto as lt
# from으로 특정 함수만 import 가능
from module_lotto import my_num, verify, lotto

if __name__ == "__main__":
    num = lt.my_num() # 사용자 번호 입력
    lotto=lt.lotto() # 로또번호 생성
    verified = lt.verify(lotto, num) # 일치하는 숫자
    print(f"이번주 로또 번호 {lotto}")
    print(f"내가 선택한 번호 {num}")
    print(f"일치하는 숫자 : {verified}")