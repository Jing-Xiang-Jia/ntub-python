hight = float(input("請輸入身高："))
weight = float(input("請輸入體重："))
seconds = float(input("請輸入跑100公尺秒數："))
BMI = weight / (hight/100) ** 2
if BMI >= 19 and BMI <= 21 or seconds <= 13.5 :
    print("BMI:",BMI,"符合條件")
else :
    print("BMI:",BMI,"不符合條件")

