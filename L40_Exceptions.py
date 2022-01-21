# Exception Handling is used when we expect that a certain type of error can come in the particular section
# that can terminate the whole code. So we use try except to display an appropriate message when an error occurs
# this prevents the code from terminating & rest of the functions work properly


# Example:

try:
    age = int(input("Age: "))       # Here we want the user to input an integer but if he enters anything else then
    print(age)                      # a ValueError can come, so we put this whole in try block, if any error comes of ValueError Type
except ValueError:                  # then the code written in the except block is executed
    print("Invalid Value")

# We can have multiple except block, for differnt exceptions

try:
    age = int(input("Age > "))
    income = 20000
    risk = income/age           # Here if the user enters 0 then error will come so we create another except block to handle it
    print(age)
    print(risk)

except ValueError:
    print("Invalid Value")
except ZeroDivisionError:
    print("Age cannot be zero")