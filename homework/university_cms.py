class Person:
    __shared_attr = {
        'name': 'Joe',
        'surname': 'Doe',
        'age': 18,
        'email': ''
    }
    def __init__(self):
        self.__dict__ = Person.__shared_attr

class Teacher(Person):
    def __init__(self, name, surname, position):
        self.name = name
        self.surname = surname
        self.position = position
    
    def __make_university_email(self):
        self.email = f'{self.name}.{self.surname}@university.com'.lower()
        return self.email
    def get_data(self):
        return f' Name: {self.name}\n Surname: {self.surname}\n E-mail: {self.__make_university_email()}'

class Student(Person):
    pass


st1 = Student()
tc1 = Teacher("Bob", "Dilan", "professor")

print(tc1.get_data())