# Loops in Python can also have a else block
# Syntax: while condition:
#             ...
#             updation

i = 1
j = 1
while(i<=5):
    print(" "*int(5-j), end="")
    a=2*j-1
    print("*"*a)
    j+=1
    i+=1
print("Done")

