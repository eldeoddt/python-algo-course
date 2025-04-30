stu=["정우람", "박으뜸", "배힘찬", "천영웅",
     "신석기", "배민규", "전민수", "박건우", "박찬호", "이승엽"]
print("시나리오 #1",stu)
print()
stu.sort()
print("시나리오 #2",stu)
print()
stu.remove("박찬호")
print("시나리오 #3",stu)
print()
print("시나리오 #4",stu[:3])
print()
stu.append("이병규")
stu.sort()
print("시나리오 #5",stu)
print()
stu.reverse()
print("시나리오 #6",stu)
print()
# 교수님 풀이
for i in range(len(stu)):
    if stu[i] == "정우람":
        stu[i] = "정잘남"
# 내 풀이
# id=stu.index("정우람")
# stu.pop(id)
# stu.insert(id, "정잘남")
print("시나리오 #7",stu)