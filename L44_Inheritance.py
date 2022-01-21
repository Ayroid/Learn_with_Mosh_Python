# Inheritance means passing member function from parent class to derived classes

class Mammal:                       # Parent Class
    def walk(self):
        print("Walk")


class Dog(Mammal):                  # Derived Class
    def bark(self):
        print("Bark")


class Cat(Mammal):                  # Derived Class
    def meow(self):
        print("Meow")


d1 = Dog()
d1.walk()
d1.bark()

c1 = Cat()
c1.walk()
c1.meow()


