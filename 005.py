code = input()
num = input()
num = int(num)
if code == "A":
    price = 155 * num
elif code == "B":
    price = 165 * num
elif code == "C":
    price = 175 * num
elif code == "D":
    price = 185 * num
print(f"{price:,}元")