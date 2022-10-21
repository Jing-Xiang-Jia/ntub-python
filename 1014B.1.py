num = str(input(""))
s2 = num.split(",")
s3 = (k.strip()  for k in s2)
s4= ["A","B","C"]
s5=["0","1","2"]
s6= ["X","Y","Z"]
s7=["7","8","9"]
count=0
for num in s3:
    if num[0] in s4 and num[-1] in s5  :
        count+=1000
    elif num[0] in s6 and num[-1] in s7  :
        count+=1000
print(f"{count:,.0f}元")


