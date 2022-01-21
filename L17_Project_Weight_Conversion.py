 # Convert Weight from Pounds to Kilograms & Vice Versa

weight = input("Weight: ")
wgt = input("(K)gs or (L)bs ")
conversion=""

if(wgt.upper()=="K"):
     conversion = int(weight)*2.205
     print(f"You are {conversion} pounds")
elif(wgt.upper()=="L"):
    conversion = int(weight)*0.454
    print(f"You are {conversion} pounds")
else:
    print("Wrong Input")

