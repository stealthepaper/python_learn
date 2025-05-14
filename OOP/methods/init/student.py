class Student:
    def __init__(self, name):
        self.name = name
        self.course = 1
        self.marks = []

g = Student("Kelly")
print(g.__dict__)