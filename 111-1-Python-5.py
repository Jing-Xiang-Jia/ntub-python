a = str(input("請輸入系別："))
Chinese = int(input("請輸入國文分數"))
English = int(input("請輸入英文分數"))
Math = int(input("請輸入數學分數"))
if a == "1" :
    total = Chinese * 1.5 +  English * 2 + Math * 1.5
elif a =="2":
    total = Chinese * 2 + English * 1.5 + Math * 1
elif a == "3":
    total = Chinese * 1.5 + English * 1.5 + Math * 1
elif a == "4" :
    total = Chinese * 1 + English * 1 + Math * 2
print(total)
