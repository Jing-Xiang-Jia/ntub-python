#輸入兩行
price = input().split(',')
amount = input().split(',')

#將list中str轉成int
price=[int(k) for k in price]
amount=[int(k) for k in amount]

#計算
total = 0

for p, a in zip(price,amount):
    total += p*a

#結果
print(total)