class Person:
    def __init__(self, name, sex):
        self.name = name
        self.sex = sex

    def talk(self):
        print(f"Hi, I am {self.name}")
        print(f" I am {self.sex}")


katrin = Person("Kathrin Smith", "Female")
katrin.talk()
john = Person("John Smith", "Male")
john.talk()
