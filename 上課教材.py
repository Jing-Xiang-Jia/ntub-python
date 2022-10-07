coupon = input("折價卷")
price = int(input("價格"))
amount = int(input("數量"))
total = price * amount
if coupon[0] in ("A","B","c"):
    if total >= 2000:
        total *= 0.8
    elif total >= 1000:
        total *= 0.9
if coupon[0] in ("D","E"):
    if total >= 3000:
        total *= 0.7
    else:
        total *= 0.85
print(f"{total:,.0f}元")

        