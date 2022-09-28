set_area = str(input("請輸入座位區:"))
people = int(input("請輸入人數:"))
if set_area == "A" or set_area =="C" or set_area =="E" or set_area =="F" or set_area =="K" :
    total = 350 * people
else:
    total = 550 * people
print(f"共{total:,.0f}元")