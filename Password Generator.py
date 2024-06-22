#Password generator 
import random 
print("Welcome to the world of password generator")
print()
randomcharacters="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#%&*"
noofpassword=int(input("How many passwords do you require? "))
lenofpassword=int(input("Enter your length of password: "))
print("***The passwords are below*** ")
for i in range(noofpassword):
    pd=""
    for j in range(lenofpassword):
        pd+=random.choice(randomcharacters)
    print(pd)
        
