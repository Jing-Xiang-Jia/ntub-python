ch = input()
en = input()
ch=int(ch)
en=int(en)

if (ch+en)/2 >= 90:
    print("A")
elif (ch+en)/2 >= 80:
    print("B")
elif (ch+en)/2 >= 70:
    print("C")
elif (ch+en)/2 >= 60:
    print("D")
else:
    print("E")
