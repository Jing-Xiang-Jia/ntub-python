ticket_num = str(input("請輸入票號："))
people = int(input("請輸入人數："))
if not "T" in ticket_num :
    total =  people * 500
elif not "M" in ticket_num :
    total =  people * 500
elif not "L" in ticket_num :
    total =  people * 500
elif not "N" in ticket_num :
    total =  people * 500
else: 
    total =  people * 400
print(total)

#未完成
