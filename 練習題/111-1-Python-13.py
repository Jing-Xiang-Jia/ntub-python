hight = float(input("請輸入身高(m)："))
weight = float(input("請輸入體重(kg)："))
bmi = weight/hight**2
if bmi >= 18.5 and bmi <= 24 :
    print("BMI:",bmi,",正常")
elif bmi > 24 :
    print("BMI:",bmi,",太重")
else:
    print("BMI:",bmi,",太輕")
