set_number = int(input("請輸入座位號碼1~20:"))
people = int(input("請輸入人數:"))
if set_number % 3 != 0:
    total = 500 * people
else:
     total = 400 * people
print(f"共{total:,.0f}元")
    
