#輸入兩行
A = input().split(',') #標準答案
B = input().split(',')#考生的答案

#將list中的str轉成int
A=[k.strip() for k in A]
B =[k.strip() for k in B]

#計算
total = 0


for C1,C2 in zip(A, B):
    if C1==C2:
        total +=10

        
print(total)