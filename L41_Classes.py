# Classes can have functions & attributes
# Names of a class begins with a captial letter & doesn't use underscores, we can seperate words by capital letters

class Point:
    def move(self):
        print("move")
    
    def draw(self):
        print("draw")


point1 = Point()
point1.draw()
point1.move()
point1.x = 10
point1.y = 20
print(point1.x)
print(point1.y)

