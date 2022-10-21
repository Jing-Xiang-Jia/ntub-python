#輸入兩行
time = input().split(',')
human = input().split(',')

#將list中str轉成int
time=[int(k) for k in time]
human=[int(k) for k in human]

#計算
total = 0

for p,a in zip (human,time):
    if a == 1:
        total+= 500*p
    elif a == 2:
        total+=800*p
    elif a == 3:
        total+= 600*p
#結果
print(f"{total:,.0f}元")