ticket = input("票號").split(",")
print(ticket)
s3 = (t.strip() for t in ticket)
print(s3)

cnt = 0
for s in s3:
    if len(s)==4 and s.count("A") >= 1:
        cnt+=1
print(cnt)