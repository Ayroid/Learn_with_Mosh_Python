class Point:
    def __init__(self,x,y):         # Constructor to Initialize Value to variables of objects
        self.x=x
        self.y=y

    def move(self):
        print("move")
    
    def draw(self):
        print("draw")


point1 = Point(10,20)               # Calling the constructor with arguments
point1.x=12                         # Changing the value of point.x
print(point1.x)
print(point1.y)