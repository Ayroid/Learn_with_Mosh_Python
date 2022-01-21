# Design a code that moves or stop the car based on user's input
answer = ""
car = 0
while(answer.upper()!="QUIT"):
    answer = input("> ").upper()
    if(answer=="HELP"):
        print("Enter:")
        print("Start - Start the car")
        print("Stop  - Stop the car")
        print("Quit  - Exit the game")
    if(answer=="START"):
        if(car == 0):
            car = 1
            print("Car started...Ready to go!")
        else:
            print("Car is Already Running.")
    elif(answer=="STOP"):
        if(car == 1):
            car = 0
            print("Car Stopped.")
        else:
            print("Car is already Stopped.")
    elif(answer=="QUIT"):
        break
    else:
        print("I don't understand that... Enter Help.")