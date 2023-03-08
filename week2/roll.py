print("welcome to the rollercoaster")
heigth=int(input("enter your heigh in cm"))
if heigth >= 120:
    print("u can enter")
    age=int(input("enter age"))
    if age >=18:
        print("adult ticket price : $30")
    elif age >=13:
        print("teen ticket price : $15")
    else:
        print("child prices : $10")   
    pic=bool(input("do u want bill or not"))
    if pic:
        print("+$3 for the pics")


else:
    print("grow up")#
