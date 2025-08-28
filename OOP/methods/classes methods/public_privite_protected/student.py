class Student:
    def __init__(self, name, age, branch):
        self.__name = name
        self.__age = age
        self.__branch = branch

    def __display_details(self):
        print(f'Имя: {self.__name}\nВозраст: {self.__age}\nНаправление: {self.__branch}')
    
    def access_private_method(self):
        return self.__display_details()


# adam = Student("Adam Smith", 25, "Information Technology")
# adam.access_private_method()

piter = Student("Piter Parker", 34, "Information Security")
piter.access_private_method()
print(piter._Student__branch)
print(piter._Student__name)
print(piter._Student__age)
piter._Student__display_details()