print("welcome to bmi calculator")
h=input("enter height")
w=input("enter weight")
bmi=int(w)/(float(h)**2)
print(round(bmi,2))
if bmi < 18.5:
    print("underweight")
elif 18.5<bmi<25:
    print("normal weight")
elif bmi >25:
    print("overweight")        
