class Constructor:
    def display(self):
        print(self.__dict__)
    def add_atribute(self, name, value):
        self.__setattr__(name, value)

obj1 = Constructor()
obj1.display()
obj1.add_atribute('color', 'red')
obj1.add_atribute('width', 20)
obj1.display()
print()
obj2 = Constructor()
obj3 = Constructor()

obj2.display()
obj3.display()

obj2.add_atribute('height', 100)

obj3.add_atribute('a', 100)
obj3.add_atribute('b', 300)
obj3.add_atribute('c', 200)
obj3.add_atribute('b', 1)

obj2.display()
obj3.display()