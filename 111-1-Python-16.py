chinese = int(input("請輸入國文分數："))
english = int(input("請輸入英文分數："))
math = int(input("請輸入數學分數："))
if chinese >= 90 and (chinese+english+math)/3 >=90 :
    print("符合資優生標準")
else:
    print("不符合資優生標準")