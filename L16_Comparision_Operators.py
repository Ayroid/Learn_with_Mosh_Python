# Comparison Operators
# >  - Greater than
# >= - Greater than equal to
# <  - Less than
# <= - Less than equal to
# == - Equality
# != - Not Equal to

# Question- If name is less than 3 characters long, print name must be at least 3 Characters long
#           otherwise if it's more than 50, print name can be a maximum of 50 Characters
#           otherwise, print Name looks Good!

name=input("Enter Name ")
print(name)
length = int(len(name))
if(length<3):
    print("Name must be 3 Characters Long")
elif(length>50):
    print("Name can be a maximum of 50 Characters")
else:
    print("Name looks Good!")