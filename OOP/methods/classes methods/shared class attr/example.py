class Cat:
    def __init__(self, breed, color):
        self.breed = breed
        self.color = color

cat1 = Cat('siam', 'grey')
cat2 = Cat('pers', 'black')

# print(cat1.__dict__)
# print(cat2.__dict__)
# print(id(cat1.__dict__), id(cat2.__dict__))


class Dog:
    __shared_attr = {
        'breed': 'maltipoo',
        'color': 'white'
    }

    def __init__(self):
        self.__dict__ = Dog.__shared_attr


dog1 = Dog() 
dog2 = Dog()
print(dog1.__dict__)
print(dog2.__dict__)
print(id(dog1.__dict__), id(dog2.__dict__))