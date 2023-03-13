marks=input("enter the marks").split()
for n in range(0,len(marks)):
    marks[n]=int(marks[n])
# print(marks,"\n")    
print("The highest score is",max(marks))
high=0
for i in marks:
    if i>high:
        high=i
print("highest score is ",high)