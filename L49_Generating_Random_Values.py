# Here we learn't about how we can use the inbuilt modules in Python
# As an example we will import a module to generate random values

import random 

for i in range(3):
    print(f"Random Numeber Between 1 & 0 is {random.random()}")

print(f"Random Number between 10 & 20 is {random.randint(10,20)}")

members = ["Ayush","Cheenu","Piyush","Gunnu","Nitya"]
leader = random.choice(members)
print(f"{leader} is the Leader")