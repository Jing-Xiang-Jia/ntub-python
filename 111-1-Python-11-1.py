set_area = str(input("請輸入座位區:"))
people = int(input("請輸入人數:"))
area = ["A","C","E","F","K"]
if set_area in area:
    total = 350 * people
    print(f"共{total:,.0f}元")
else:
    total = 550 * people
    print(f"共{total:,.0f}元")
        