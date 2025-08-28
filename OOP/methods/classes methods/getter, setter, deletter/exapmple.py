# class Person:
#     def __init__(self, name, age):
#         self._name = name
#         self._age = age
    
#     def get_name(self):
#         return self._name
    
#     def set_name(self, value):
#         if isinstance(value, str) and len(value) > 0:
#             self._name = value
#         else:
#             raise ValueError('Имя должно быть непустой строкой')

# p = Person('Artem', 33)
# print(getattr(p, '_name'))  
# print(getattr(p, '_age')) 
# p.set_name(100)


# class Person:
#     def __init__(self, name, age):
#         self._name = name
#         self._age = age
    
#     def get_name(self):
#         return self._name
    
#     def set_name(self, value):
#         if isinstance(value, str) and len(value)>0:
#             self._name = value
#         else:
#             raise ValueError('Имя должно быть непустой строкой')
    
#     name = property(fget=get_name, fset=set_name)


# p = Person('Artem', 33)
# print(p.name)
# p.name = 'Ivan'
# print(p.name)

# print(Person.__dict__)

class Student:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self._name

    def set_name(self, value):
        self._name = value.upper()

    name = property(fget=get_name)

student = Student(name="Kevin")
print(student.name)
student.name = 'Kev'
print(student.name)