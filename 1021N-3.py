#輸入兩行
min = input().split(',')
hua = input().split(',')

#將list中str轉成int
min=[int(k) for k in min]
hua=[int(k) for k in hua]

#計算

p = 0
a = 0

for j,k in zip (min,hua):
    if j > k:
        p += 1
    elif j < k:
        a+=1

if p > a:
    print("王小明")
elif a > p:
    print("陳小華")
elif p == a:
    print('平手')