# class BankAccount:
#     def __init__(self, name, passport, balance):
#         self._name = name
#         self._passport = passport
#         self._balance = balance
#     def print_protected_data(self):
#         print (self._balance, self._name, self._passport)

# account1 = BankAccount('Bob', 100000, 45484564654)
# account1.print_protected_data()
# print(account1._name)      
# print(account1._balance)   
# print(account1._passport)


# class BankAccount:
#     def __init__(self, name, passport, balance):
#         self.__name = name
#         self.__passport = passport
#         self.__balance = balance
#     def __print_protected_data(self):
#         print('work privite method')
#         print (self.__balance, self.__name, self.__passport)
    
#     def public_call(self):
#       print('work public method')
#       self.__print_protected_data()

# account1 = BankAccount('Bob', 100000, 45484564654)
# account1.public_call()


class Student:
    def __init__(self, name):
        self.name = name
        self._course = 1
        self.__marks = []

studen1 = Student('Kevin')
studen1._course = 2
print(studen1._course)
print(studen1.__dict__)
studen1.__dict__['__marks'] = [5, 4]
print(studen1.__dict__)
print(studen1.__marks)
