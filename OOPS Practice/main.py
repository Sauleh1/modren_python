class Calc:
    name: str = "Hello world"
    age: int = 12
    Class: str = "VII-O-C" 
    def __init__(self, a, b, c):
        self.name = a
        self.age = b
        self.Class = c
    
Student1 = Calc("Mohammad Sauleh", 12, "Jmaat Haftam")

Student1.age = Student1.age + 1


