class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age
    
    def get_name(self):
        return self._name
    
    def set_name(self, value):
        if isinstance(value, str) and len(value) > 0:
            self._name = value
        else:
            raise ValueError('Имя должно быть непустой строкой')

p = Person('Artem', 33)
print(getattr(p, '_name'))  
print(getattr(p, '_age')) 
p.set_name(100)