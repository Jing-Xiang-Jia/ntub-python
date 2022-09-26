drink = input("飲料：")
cups = int(input("杯數："))
if drink == "A" :
    total = 50 * cups
if drink == "B" :
    total = 60 * cups
if drink == "C" :
    total = 70 * cups


print(f'{total:,.0f}元')



