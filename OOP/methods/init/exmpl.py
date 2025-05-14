class Car_one:
    def __init__(self, new_model, new_color, new_engine, new_hourse_power):
        self.engine = new_engine
        self.model = new_model
        self.color = new_color
        self.hourse_power = new_hourse_power
    def drive(self):
        print(f'Let`s go {self.model} - {self.engine}')
    def get_power(self):
        print(f'{self.model} = {self.hourse_power} HP')
    def get_color(self):
        print(f'Color of {self.model} - {self.color}')


class Car_two:
    def __init__(self, new_mod = 'Tesla', new_col = 'White', new_eng = 1.3, new_pow = 231):
        self.mod = new_mod
        self.col = new_col
        self.eng = new_eng
        self.pow = new_pow
    def ryan_gosling(self):
        if self.pow > 150:
            print(f'{self.mod} - vroom vroom')
        else:
            print(f'{self.mod} - buzzz buzz')
    def engine_power(self):
        print(f'{self.mod} have {self.eng} and it`s {self.pow} HP')
    def car_color(self):
        print(f'{self.mod} is {self.col} color')

bmw_3 = Car_one('BMW', 3, 500, 'black')  # вызывается метод __init__
print(bmw_3.__dict__)
print('-----')
# audi_q4 = Car_one('Audi', 2.5, 400, 'red')  # вызывается метод __init__
# print(audi_q4.__dict__)
# audi_q4.get_power()
# audi_q4.drive()

honda_a66 = Car_two('Horda', 'black')
print(honda_a66.__dict__)