#輸入兩行
A = input().split(',') #王出牌
B = input().split(',')#陳出牌

#將list中的str轉成int
A=[int(k) for k in A]
B =[int(k) for k in B]

#計算
p1 = 0
p2 = 0


for C1,C2 in zip(A, B):
    if C1==1:
        p1 +=1
    elif C2==1:
        p2 +=1
    elif C1>C2:
        p1 +=1
    elif C2>C1:
        p2 +=1

#輸出/判斷
if p1>p2:
    print('王小明')
elif p2>p1:
    print('陳小華')
elif p1==p2:
    print('平手')