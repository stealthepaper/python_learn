class Dog:
    def __init__(self, name, color):
        self.name = name
        self.color = color.capitalize()
    
    def bark(self):
        match self:
            case 'White'| 'Brown':
                return 'Woof!'
            case 'Red':
                return 'Woof! Woof!'
            case 'Black':
                return 'Woof! Woof! Woof!'

d1 = Dog('s', 'white')
print(d1.bark())

d2 = Dog('t', 'Black')
print(d2.bark())


