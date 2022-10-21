num = str(input("")).split(",")
s3 = (k.strip()  for k in num)
count=0
x = [0]+[1]+[2]
for num in s3:
    x=num[0]+num[1]+num[2]
    if len(num)==8 and  x in ["109","110","111"]  and num[3] in ["4","5"] and num[4]in["6"]:
        count+=1
print(count)


