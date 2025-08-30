class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Guardian(Human):
    def __init__(self, name, age, kids):
        super().__init__(name, age)
        self.kids = kids

guardian1 = Guardian("Domingo", 20, 17)
print(guardian1.kids)
print(guardian1.age)
print(guardian1.name)

class Teacher(Human):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject

class Professor(Teacher):
    

