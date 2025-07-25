class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def sayHello(self):
        print("Hello")
        
    def sayBye(self):
        print("Bye")
        
teacher = Person('Emily', 20)
teacher.sayBye()