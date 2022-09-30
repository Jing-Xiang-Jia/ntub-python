a = int(input("杯數:"))
運費= a
total = (55 * a ) + a
if a >= 4 : 
  total = (55*a) +0
else :
    total = (55*a) +60
print(f'{total:,.0f}元')

