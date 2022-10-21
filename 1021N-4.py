#輸入兩行
area = input().split(',')
amount = input().split(',')

#將list中str轉成int
area=[k.strip() for k in area]
amount=[int(k) for k in amount]

#計算

total = 0

for ar,am in zip (area,amount):

    if ar[0] == "A":
        if "0"<=ar[1]<="5": 
            total+=1500*am
        elif ar[1] in ["6","7","8","9"]:
            total +=1200*am
    elif ar[0] == "B":
        if ar[1] in ["0","1","2"]: 
            total+=1000*am
        elif ar[1] in ["3","4","5"]:
            total +=900*am
        elif ar[1] in ["6","7","8","9"]:
            total+=800*am

    elif ar[0] == "C":
        if ar[1] in ["0","3","4"]: 
            total+=750*am
        elif ar[1] in ["1","5","8","9"]:
            total +=600*am
        elif ar[1] in ["2","6","7"]:
            total +=500*am

print(f"{total:,.0f}元")