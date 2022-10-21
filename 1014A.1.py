num = input("")
s2 = num.split(",")
s3 = (int(k) for k in s2)
count=0
for num in s3:
    if num >= 90 :
        count+=3
    elif num >= 80 :
        count+=2
    elif num >= 70 :
        count+=1
print(count)


