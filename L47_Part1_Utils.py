# L47 Part 1 & 2 are to practice functions & Modules together
# In Part1 we define the function & then we import it in Part2 then use the function 

def findmax(num):
    max = num[0]
    for i in num:
        if i > max:
            max = i
    return max
