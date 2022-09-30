#判斷4
id = input("身分證字號：")
list=["0","2","4"]
if id[-1] in list :
    print("中獎")
else:
    print("沒中獎")
#判斷5
id = input("身分證字號：")
list=("0","2","4")
if id[-1] in list :
    print("中獎")
else:
    print("沒中獎")

#turple型別
a = ("2","4","6","8")
print(a)
print(a[1])
print(type(a))

#list型別
a = ["2","4","6","8"]
print(a)
print(type(a))
a[1]=5
print(a)


