#輸入兩行
right = input().split(',')
student = input().split(',')

#將list中str轉成int
right=[k.strip() for k in right]
student=[k.strip() for k in student]

#計算

total = 0

for ri,stu in zip (right,student):
    if ri == stu:
        total += 10

print(total)