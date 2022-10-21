num = input().split(",")
s3 = [k.strip()  for k in num]
count=0
for c in s3:
    if len(c)>=6 and (c.count("A")>=1 or c.count("0")>=1):
        count+=1
print(count)


