# Here we learnt about the various methods related to a list

numbers = [5,2,4,6,3,8]
num = [1,7,9]

numbers.append(4)                   # To enter an element at last position
print(numbers)

print(numbers.copy())               # To return a copy of list

numbers.insert(1,7)                 # To insert an element at a positon
print(numbers)

numbers.sort()                      # To sort a list
print(numbers)

numbers.reverse()                   # To reverse a list
print(numbers)

print(numbers.count(2))             # To count the occurence of element passed

print(numbers.index(6))             # To return the first index of the element

numbers = numbers.__add__(num)      # To concatinate 2 Lists
print(numbers)

print(numbers.pop())                # Removes an element from the position

(numbers.clear())                   # To delete all elements of a list
print(numbers)



