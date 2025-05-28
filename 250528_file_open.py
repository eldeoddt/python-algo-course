file = open("e:/class/python/fileTest.txt", "w")
result = file.write("hello python ~")
print("type of result: ", type(result))
print("result: ", result)
file.close()
# type of result:  <class 'int'>
# result:  14

# -> write() 함수는 쓰기 실행 후 문자의 개수를 반환한다. 공백 포함이다.

file = open("e:/class/python/fileTest.txt", "r")
result = file.read()
print("type of result: ", type(result))
print("result: ", result)
file.close()
# type of result:  <class 'str'>
# result:  hello python ~

# -> read로 읽은 데이터는 항상 string이다.