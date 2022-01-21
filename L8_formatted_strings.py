first = "John"
last = "Smith"
message = first + ( " [")+last+("] is a coder")             # Normal Method
print(message)
msg = f"{first} [{last}] is a coder"                        # Formatetted String - It is started with f then output is written under inverted commas. 
print(msg)                                                  #                      It helps in visulazing the Output better. {}-These are called placeholders