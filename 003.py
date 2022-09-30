code = str(input("請輸入(A、B、C、D):"))
num = int(input("請輸入數量："))
if code == "A":
    price = 155 * num
elif code == "B":
    price = 165 * num
elif code == "C":
    price = 175 * num
elif code == "D":
    price = 185 * num
print(f"{price: .0f}元")


