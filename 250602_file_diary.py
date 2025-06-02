from time import strftime, localtime
day = strftime('%Y-%m-%d', localtime())
time = strftime('%H:%M:%S', localtime())
content = input(f"[{day} {time}] ")

# diary.txt 파일에 일기를 작성하고 일기 내용을 읽어서 출력
file = open("e:/class/python/diary.txt", "a")
file.write(f"[{day} {time}] {content}\n")
file.close()

print()
file = open("e:/class/python/diary.txt", "r")
result = file.read()
print(f"{'-'*20} 일기장 {'-'*20}\n{result}")
file.close()