#    Создайте класс Dog, у которого есть:
# метод __init__, принимающий имя и возраст собаки и сохраняющий их в атрибуты name и age;
# метод description, который возвращает строку в виде «{name} is {age} years old»;
# метод speak принимающий один аргумент, который возвращает строку вида «{name} says {sound}».

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def description(self):
        return f'{self.name} is {self.age} years old'

    def speak(self, sound):
        return f'{self.name} says {sound}'

# Ниже код для проверки класса Dog
curt = Dog("Curt", 4)
assert isinstance(curt, Dog)
assert curt.name == 'Curt'
assert curt.age == 4
assert curt.description() == 'Curt is 4 years old'
assert curt.speak("Wo") == 'Curt says Wo'
assert curt.speak("Bow") == 'Curt says Bow'

jack = Dog("Jack", 12)
assert isinstance(curt, Dog)
assert jack.name == 'Jack'
assert jack.age == 12
assert jack.description() == 'Jack is 12 years old'
assert jack.speak("Woof Woof") == 'Jack says Woof Woof'
assert jack.speak("Bow Wow") == 'Jack says Bow Wow'

assert Dog('Karl', 6).description() == 'Karl is 6 years old'        
print('Good')