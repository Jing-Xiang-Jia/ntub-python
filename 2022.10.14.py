score = input("成績")

s2 = score.split(",")
print(s2)
print(type(s2))
#將字串分割成list
score = input ("成績：").split(",")
#將list的字串內容轉成int
s3 = [int(k) for k in s2]
print(s3)
#逐一取出list內容並判斷
cnt = 0

for s in s3 :
    if s < 60:
        cnt+=1
#印出結果
print(cnt)