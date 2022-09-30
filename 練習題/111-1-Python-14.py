age = int(input("請輸入年齡："))
purchasing＿price = int(input("請輸入購買金額："))
if age >= 17 and age < 24 :
    total = purchasing＿price - 300
elif age >= 60 and age < 80 :
    total = purchasing＿price - 500
else:
    total = purchasing＿price
print(f"{total:,.0f}元")
