class Pesin:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def greet(self):
        print("Wagwan")

class Nurse(Pesin):
    def __init__(self, name, age):
        super().__init__("Nurse" + name, age)
    def intro(self):
        print("Wagwan I am ", self.name)

person1 = Nurse("Emily", 20)
person2 = Pesin("Tom", 77)

person1.intro()
person2.greet()

class Teacher(Pesin):
    def __init__(self, name, age):

        super().__init__("Teacher" + name, age)










'''
class Pesin:
    name = "Sam"
    def greet(self):
        print("Hi")

p = Pesin()
p.greet()






class Pesin:
    def__init__(self, name, age)
    self.name = name
    self.age = age

    def greet(self):
        print("Hi")

class Student(Pesin):
    def __init__(self, name, age, major):
    super().__init__(name, age)
        self.major = major
        
student = Student("Sticky", 29)
print(student.major)
student.greet()
    
'''
