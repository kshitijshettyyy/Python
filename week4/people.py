import random
# names=["kshitij","veda","rishi","uday","prajwal"]
# print(names)
names_string=input("enter the names \n")
names=names_string.split(" ")
lenght=len(names)
r_n=random.randint(0,lenght-1)
print(names[r_n])