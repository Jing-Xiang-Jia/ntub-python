height = float(input())
amount = float(input())
if height >= 190 :
    heightnum = 50
elif height >= 180 and height < 190 :
    heightnum = 40
elif height >= 175 and height < 180:
    heightnum = 35
elif height <175:
    heightnum = 30

if amount >= 195 :
    amountnum = 50
elif amount >= 185 and amount< 195 :
    amountnum = 40
elif amount <185 :
    amountnum = 30

total = amountnum +heightnum
if amountnum >=40 and  heightnum >=40:
    total +=10
print(total)
    




