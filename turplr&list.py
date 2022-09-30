#turple型別(immutable，初值設定後不可更改)
a = ("2","4","6","8")
print(a)
print(a[1])
print(type(a))

#list型別(mutable，初值設定後可更改)
a = ["2","4","6","8"]
print(a)
print(type(a))
a[1]=5  #替換第2個數字
print(a)




