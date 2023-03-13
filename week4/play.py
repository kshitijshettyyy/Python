row1=["⬜","⬜","⬜"]
row2=["⬜","⬜","⬜"]
row3=["⬜","⬜","⬜"]
map=[row1,row2,row3]
print(f"{row1}\n{row2}\n{row3}")
i=1
while(i!=0):
    choice=input("enter the position")
    row=int(choice[0])
    col=int(choice[1])
    map[row][col]="🟥"
    print(f"{row1}\n{row2}\n{row3}")
