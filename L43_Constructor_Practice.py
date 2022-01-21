class Person:
    def __init__(self,name):
        self.name = name

    def talk(self):
        print(f"Hi, I am {self.name}")


ayush = Person("Ayush Singh Kushwah")
cheenu = Person("Cheenu")
ayush.talk()
cheenu.talk()