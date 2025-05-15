# Реализуйте класс Numbers, который предназначен для хранения произвольного количества чисел. Данный класс должен содержать:
 # метод __init__, принимающий произвольное количество чисел и сохраняющий их внутри экземпляра;
 # метод add_number, которой принимает числовое значение и добавляет его в конец коллекции экземпляра;
 # метод get_positive, который возвращает список всех положительных чисел из коллекции экземпляра;
 # метод get_negative, который возвращает список всех отрицательных чисел из коллекции экземпляра;
 # метод get_zeroes,  который возвращает список всех нулевых значений из коллекции экземпляра.

class Numbers:
    def __init__(self, *args):
        self.numders = list(args)
    
    def add_number(self, number):
        self.numders.append(number)
    
    def get_positive(self):
        posititve_numbers = [i for i in self.numders if i > 0]
        return posititve_numbers

    def get_negative(self):
        negative_numbers = [i for i in self.numders if i < 0]
        return negative_numbers

    def get_zeroes(self):
        zeroes_numbers = [i for i in self.numders if i == 0]
        return zeroes_numbers


# nums = Numbers(1, 2, -4, -5, 3)

# print(nums.get_positive())
# print(nums.get_negative())
# print(nums.get_zeroes())

# nums = Numbers(10, 20, 30, 0, 0, 5)

# print(nums.get_positive())
# print(nums.get_zeroes())
# nums.add_number(100)
# nums.add_number(0)
# nums.add_number(7)
# print(nums.get_positive())
# print(nums.get_zeroes())

# nums = Numbers(7, 8, 9)
# nums_2 = Numbers(7, 8, 9)

# nums.add_number(10)
# nums_2.add_number(11)
# nums_2.add_number(12)
# print(nums.get_positive())
# print(nums_2.get_positive())

nums = Numbers()
print(nums.get_positive())
print(nums.get_negative())
print(nums.get_zeroes())

nums.add_number(5)
nums.add_number(3)
nums.add_number(4)

print(nums.get_positive())
print(nums.get_negative())
print(nums.get_zeroes())