print("welcome to tip calc")
bill=input("what was the bill? $")
perc=input("what percentage tip would you like to give?")
no=input("how many people to split the bill")
tip=int(bill)*int(perc)/100
amt=int(bill)+int(tip)
split=int(amt)/int(no)
print("amout everyone has to pay ",split)