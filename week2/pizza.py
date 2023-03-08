size=input("size")
pep=input("peparoni?")
cheeze=input("cheeze?")
cost=0
if size=="L":
    cost=int(cost)+25
elif size=="M":
    cost+=20
else:
    cost+=15
if pep=="Y":
    if(size=="S"):
        cost+=2
    else:
        cost+=3        
if cheeze=="Y":
    cost+=1
print(cost)