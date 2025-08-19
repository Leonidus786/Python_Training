

Age = int(input("Enter your age: "))


if Age >= 18 and Age < 55:
    print("Allowed to make a driving license")
elif Age>=12 and Age<18 :
    print("you are a teenager")
elif Age>= 55:
    print("You can't have a driving license")
else:
    print("you are a kid")
 