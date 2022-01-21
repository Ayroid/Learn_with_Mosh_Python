# Tuples are similar to lists but their values cannot be changed or modified
# which means you cannot use methods like insert(), append(), remove(), etc.
# Elements of a Tuple are defined inside () rather than [] which are used by lists.
# Usage of () seperates a Tuple from List
# Tuples are useful when in a program you want a list of elements to stay constant throughtout the duration.

num = (1,2,3)       # This is a Tuple

print(num.index(1))
print(num.count(2)) 