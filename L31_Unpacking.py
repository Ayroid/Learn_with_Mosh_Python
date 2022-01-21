# Unpacking is similar to storing the elements of an list/tuple in seperate variables

coordinates = (1,2,3)

sum = coordinates[0]+coordinates[1]+coordinates[2]
print(sum)

# The above lines are understandable & easy to write but if we had to repeat
# them again & again, then it's a waste of time so we can assign values of elements
# of tuple/list to seperate variables as below

coordinates = (4,5,6)
x = coordinates[0]
y = coordinates[1]
z = coordinates[2]

sum = x+y+z
print(sum)

# We can achieve the same in a faster & efficient way using Unpacking

coordinates = (1,3,5)

x,y,z = coordinates     # Unpacking the elements of Tuple into variables

sum = x+y+z
print(sum)