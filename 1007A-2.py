from re import S


chinese = int(input())
english = int(input())
book = str(input())

if book == "A":
    booknum = 60
elif book == "B":
    booknum = 40
elif book == "C":
    booknum = 20
elif book == "D":
    booknum = 0

total = chinese + english +booknum
if total >= 240 :
    print("A")
elif total >= 190 and total < 240 :
    print("B")
elif total >= 150 and total < 190 :
    print("C")
else:
    print("D")