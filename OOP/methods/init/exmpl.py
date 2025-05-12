class Car:
    def __init__(self, new_model, new_color, new_engine, new_hourse_power):
        self.engine = new_engine
        self.model = new_model
        self.color = new_color
        self.hourse_power = new_hourse_power
    def drive(self):
        print(f'Let`s go {self.model} - {self.engine}')
    def get_power(self):
        print(f'{self.model} = {self.hourse_power} PC')
    def get_color(self):
        print(f'Color of {self.model} - {self.color}')

bmw_3 = Car('BMW', 3, 500, 'black')  # вызывается метод __init__
print(bmw_3.__dict__)
print('-----')
audi_q4 = Car('Audi', 2.5, 400, 'red')  # вызывается метод __init__
print(audi_q4.__dict__)
audi_q4.get_power()
audi_q4.drive()