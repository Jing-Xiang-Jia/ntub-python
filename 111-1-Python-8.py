Chinese = int(input("請輸入國文分數"))
English = int(input("請輸入英文分數"))
Math = int(input("請輸入數學分數"))
Social = int(input("請輸入社會分數"))
Technology = int(input("請輸入自然分數"))

total = Chinese + English + Math + Social + Technology

if total >= 460 and total <=500 :
    grand = "Ａ"
elif total >= 420 and total <= 459 :
    grand = "B"
elif total >= 370 and total <= 419 :
    grand = "C"
elif total >= 320 and total <= 369 :
    grand = "D"
else:
    grand = "E"

print("總分為",total,"等級為",grand)

