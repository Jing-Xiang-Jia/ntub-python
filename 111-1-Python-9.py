set = str(input("請輸入座位區："))
people= int(input("請輸入人數："))

if set != "A" :
    total = 300 * people
else :
    total = 500 * people
print(f"{total:,.0f}元")

