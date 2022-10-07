set = input()
k = input()
set = str(set)
k = int(k)

if set[-1] == "A":
    total = 12.5 * k
elif set[-1] == "B":
    total = 10.5 * k
elif set[-1] == "C":
    total = 8.5 * k

print(f"{total:,.0f}元")