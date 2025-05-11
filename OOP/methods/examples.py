class Cat:
    breed = 'pers'
    def hello(*args):
        print('Hello world from kitty')
    def show_breed(self):
        print(f'my breed is {self.breed}')
    def show_name(self):
        if hasattr(self, 'name'):
            print(f'my name is {self.name}')
        else:
            print('nothing')
    def set_value(self, value):
        self.name = value

walt = Cat()
walt.show_breed()
walt.breed = 'siam'
walt.show_breed()

mary = Cat()
mary.name = 'Mary'
mary.show_name()

bob = Cat()
bob.show_name()

tom = Cat()
tom.set_value('Tom')
tom.show_name()