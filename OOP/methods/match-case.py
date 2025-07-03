class Dog:
    def __init__(self, name, color):
        self.name = name
        self.color = color.capitalize()
    
    def bark(self):
        match self.color:
            case 'White'| 'Brown':
                return 'Woof!'
            case 'Red':
                return 'Woof! Woof!'
            case 'Black':
                return 'Woof! Woof! Woof!'
    
    def __str__(self):
        return f'name - {self.name}\ncolor - {self.color}'

d1 = Dog('s', 'White')
print(d1.bark())

d2 = Dog('t', 'Black')
print(d2)
