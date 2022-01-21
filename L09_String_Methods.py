# Methods are functions that belong specifically to the strings only whereas Functions are General & can be used with any variable type.
# Dot (.) operator is used to access the methods of the string
course = "Python for Beginners"
length=len(course)
print(course)
print(length)
print(course.upper())           # .upper() converts the string to Uppercase
print(course.lower())           # .lower() converts the string to Lowercase
print(course.capitalize())      # .capitalize() converts the first character of the string to capital & rest to lower case
print(course.find("n"))         # .find() returns the index of the first occurence of the character inside the string. It returns -1 if no character is found.
print(course.replace("Beginners","Professionals"))    # Replaces substring by another string
print("Python" in course)       # in operator returns a boolean value if the passed string is in our original string