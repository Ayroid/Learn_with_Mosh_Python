# Dictionaries are like Structures in C, they can store different datatypes in a single variable
# Variables inside a dictionary are unique just like a real life dictionary

customer = {
    "name": "Ayush Singh Kushwah",
    "age": 19,
    "is_verified": True
}

print("Customer Name:",customer["name"])
print("Customer Age:",customer["age"])
print("Verification Status:",customer["is_verified"])

# We can also use the get() function so that even if a value that doesn't exist is called
# the code will run without showing any error

print("Customer Name:",customer.get("name"))  # even if a wrong value is passed the code will run without any error

# If the value is not found then None is returned automatically but we can show a customized message if we want to

print("Customer Age:",customer.get("date_of_birth","Wrong Input"))  # As we can see date_of_birth doesn't exist in our dictionary so we can display any message we want to tell the user it doesn't exist

# We can add new key values & modify the ones that already exist really easily

customer["name"] = "Captain Ayush"
customer["birth_date"] = "15 Aug 2002"

print("Customer Name:",customer["name"])
print("Date of Birth", customer["birth_date"])