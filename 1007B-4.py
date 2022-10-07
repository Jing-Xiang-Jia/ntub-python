num = str(input())
man = int(input())
kid = int(input())
total = man *900 +kid *600
if num[0]=="A":
    if man >= 2 and kid >=2:
        total = (900*man +600*kid ) -500
    elif man +kid  >=3 :
        total = (900*man +600*kid ) -400
if num[0]=="B":
    if man >= 2 and kid >=3:
        total = (900*man +600*kid ) -650
    elif man >= 1 and kid >=2:
        total = (900*man +600*kid ) -550
if num[0]=="C":
    if man >= 2 or kid >=4:
        total = (900*man +600*kid ) -850
    elif man >= 1 or kid >=1:
        total = (900*man +600*kid ) -650
print(f"{total:,.0f}元")