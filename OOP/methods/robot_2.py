class Robot():
    def set_name(self, value):
        self.name = value
    def say_hello(self):
        if hasattr(self, 'name'):
            print(f'Hello, human! My name is {self.name}')
        else: 
            print('У робота нет имени')
    def say_bye(self):
        print('See u later alligator')

c3po = Robot()
c3po.say_hello()
c3po.set_name('R2D2')
c3po.say_hello()
c3po.say_bye()

r = Robot()
r.set_name('Chappy')
r.say_hello()

d = Robot()
d.set_name('Dendy')
d.say_hello()