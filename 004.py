price = int(input("請輸入單價"))
num = int(input("請輸入數量："))
if price * num >= 2000 :
    total = (price*num)* 0.85
elif price * num >= 1000 :
    total = (price*num)* 0.9
else :
    total = (price*num)* 0.95
print(f"{total: .0f}元")



