class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def greet(self):
        return f'Hello my name is {self.name}, ' \
                f'and I am {self.age} years old'

persons = []
persons.append(Person('Dylan', 23))
persons.append(Person('Bob', 19))
persons.append(Person('Emily', 21))

for prs in persons:
    print(prs.name, prs.age)
    print(prs.greet())
    print()
    