answer = str(input())
amount = int(input())

if answer == "Y":
    if amount <= 120:
        total = amount * 2.10
    elif amount >= 121 and amount <= 330:
        total = amount * 3.02
    elif amount >= 331 and amount <= 500:
        total = amount * 4.39
    elif amount >= 501 and amount <= 700:
        total = amount * 5.44
    elif amount >= 701 and amount <= 1000:
        total = amount * 6.16
    elif amount >= 1001:
        total = amount * 6.71
if answer == "N":
    if amount <= 150:
        total = amount * 1.95
    elif amount >= 151 and amount <= 350:
        total = amount * 2.94
    elif amount >= 351 and amount <= 520:
        total = amount * 4.21
    elif amount >= 521:
        total = amount * 5.98
print(f"{total:,.0f}元")  

