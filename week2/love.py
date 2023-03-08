name1=input("enter name 1 \n")
name1=name1.lower() 
name2=input("enter name 2 \n")
name2=name2.lower()
combo=name1+name2
t=combo.count("t")
r=combo.count("r")
u=combo.count("u")
e=combo.count("e")
l=combo.count("l")
o=combo.count("o")
v=combo.count("v")
e=combo.count("e")




true=t+r+u+e
love=l+o+v+e
love_score=int(str(true)+str(love))

if(love_score<10) or (love_score>90):
    print("ur love score is {}".format(love_score))
elif(love_score>=40)and(love_score<=50):
    print("ur score is {}".format(love_score))    
else:
    print("ur ok ok {}".format(love_score))    
