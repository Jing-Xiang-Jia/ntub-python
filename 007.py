price = input()
num = input()
price = int(price)
num = int(num)

if price * num >= 2000 :
    total = (price*num)* 0.85
elif price * num >= 1000 :
    total = (price*num)* 0.9
else :
    total = (price*num)* 0.95

total = round(total)
print(f"{total:,.0f}元")