set_area = input("請輸入座位區:")
people = int(input("請輸入人數:"))
area = ["A","C","E","F","K"]
for data in area:
    if area == data:
        total = 350 * people
    else:
        total = 550 * people
print(f"共{total:,.0f}元")