from re import A


money = int(input("請輸入銷售額："))

if money >= 100000:
    total = money * 0.215
else:
    total = money * 0.165
print(f'{total:,.0f}元')