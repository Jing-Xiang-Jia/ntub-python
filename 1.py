price = int(input("單價:"))
amount = int(input("數量:"))
total = price * amount
if total >= 2000: 
    total = total * 0.9
else :
    total = total *0.95 
print(f'{total:,.0f}元')

