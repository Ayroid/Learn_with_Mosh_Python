# While passing the arguments, they are received in the same sequence as we have passed,
# but in order to improve the readability of our code we can use keyword arguments
# in which we define that the value we passed belongs to which argument

def greet_user(first_name,last_name):
    print(f"Hello! {first_name} {last_name}")
    print("Welcome Aboard!")

print("Start")
greet_user("Ayush","Singh")   # Ayush will be assigned to first_name & Singh to last_name
print("Stop")

# But if we change their order it will received that way only, so inorder to prevent the same we can use keyword arguments

print("Start")
greet_user(last_name="Singh",first_name="Ayush")    # This way the sequence doesn't matter
print("Stop")

# If we are using both positional & keyword arguments together then we should write positional arguments first

print("Start")
greet_user("Singh",first_name="Ayush")      # If we do it the opposite way, then it shows an error
print("Stop")