pay = int(input("輸入時薪:"))
hours = int(input("輸入時數"))

if hours >= 50 :
    total = pay * hours + 35 * hours
elif hours < 50 and hours >= 30 :
    total = pay * hours + 25 * hours
elif hours < 30 and hours >= 10 :
    total = pay * hours + 10 * hours
else:
    total = pay * hours + 0
print(f'共{total:,.0f}元')






