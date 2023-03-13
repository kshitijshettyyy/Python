import random
password=[]#list of password
ans=""
print("welocme to password generator")
n_letters=int(input("how many letters?"))
n_symbols=int(input("how many symbols?"))
n_numbers=int(input("how many numbers?"))
letters=['K','k','S','s','H','h','I','i','T','t','J','j']
numbers=['1','2','3','4','5','6','7','8','9','0']
symbols=['!','$','%','?','&','^']
for char in range(1,n_letters+1):
    password+=random.choice(letters)
for sy in range(0,n_symbols):
    password+=random.choice(symbols)
for num in range(0,n_numbers):
    password+=random.choice(numbers)
random.shuffle(password)
for char in password:
    ans+=char
print(ans)    