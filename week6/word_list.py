import random
print("welcome to hangman\nu have to guess the secret word \nbut u just hv 5 lives")
word_list=["behaviour","comfortable","vinegar","important","sanvika"]
word=random.choice(word_list)
display=[]
for i in range(len(word)):
    display+='_'
mistake=0    
while mistake<5:
    letter=input("guess the letter")
    n=0
    found=0
    for i in word:
        if i==letter:
            found=1
            display[n]=letter
        n+=1
    if found==0:
        mistake+=1
    live=[]
    for i in range(0,5-mistake):
        live+='*'
    print(f"{''.join(live)}")               
    print(f"{''.join(display)}")
    flag=0
    for i in display:
        if i=="_":
            flag=1
    if flag==0:
        print("game over\n u win")
        exit()
print("error count reached\n u lose")        