import module_object_dice as rd
score=[]

# sum 출력
for j in range(3):
    num=rd.generateNum()
    score.append(sum(num))
    print(f"Gamer {j+1}: {num}\nSum of gamer{j+1}: {score[j]}")
    print("-"*30)

# sort 로 정렬
score.sort(reverse=True)
print("="*30)
for i in range(3):
    print(f"{i+1}등 : {score[i]}점", end='')
    if i == 0:
        print("\twin!!")
    else:
        print()
print("="*30)