chinese = int(input("請輸入國文分數："))
english = int(input("請輸入英文分數："))
math = int(input("請輸入數學分數："))
amount = str(input("操行(A or B or C):"))
if chinese >= 90 or (chinese+english+math)/3 >=90 or amount=="A":
    print("符合條件")
else:
    print("不符合條件")