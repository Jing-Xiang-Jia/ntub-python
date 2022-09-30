num = int(input("人數："))
area = str(input("區域："))

if area == "A" :
    total = 500*num
if area == "B" :
    total = 450*num
if area == "C" :
    total = 380*num
if area == "D" :
    total = 310*num
if area == "E" :
    total = 250*num


print(f'{total:,.0f}元')



