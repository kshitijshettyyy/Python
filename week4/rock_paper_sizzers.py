import random
mychoice=int(input("enter choice\n1=rock 2=paper 3=sizzors"))
choice2=random.randint(0,2)
cho=[1,2,3]
emo=["🖐","✊","✌"]
if mychoice==0 and choice2==2:
    print("u win")#
elif mychoice>choice2:
    print("u win")
elif choice2>mychoice:
    print("u lose")    
