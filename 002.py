id = input("身分證字號：")
m = id[-1]

#判斷1
if m=="0" or m=="2" or m=="4" :
    print("中獎")
else:
    print("沒中獎")
#判斷2
if m in ("0","2","4"):
    print("中獎")
else:
    print("沒中獎")
#判斷3
if m in ["0","2","4"]:
    print("中獎")
else:
    print("沒中獎")



