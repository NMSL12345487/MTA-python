score_list = []
num = int(input("number?"))
for i in range(num):
    score = int(input("score?"))
    score_list.append(score)
    if score_list[i]<60:
        score_list[i]=60
print("最高分",sorted(score_list)[-1])
print("最低分",sorted(score_list)[0])
