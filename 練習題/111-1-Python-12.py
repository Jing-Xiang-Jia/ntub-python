ticket_num = str(input("請輸入票號："))
people = int(input("請輸入人數："))
list = ["T","M","L","N"]
if ticket_num[0] not in list:
    total =  people * 500
else:
    total =  people * 400
print(total)
