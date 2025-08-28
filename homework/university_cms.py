class Person:
    __shared_attr = {
        'name': 'Joe',
        'surname': 'Doe',
    }
    def __init__(self):
        self.__dict__ = Person.__shared_attr

class Teacher(Person):
    def __init__(self, name, surname, position, specialization):
        self.name = name
        self.surname = surname
        self.position = position
        self.specialization = specialization
        self.__syllabus = []
    
    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        faculty_grade = {"senior lecture", "associate proressor", "professor"}
        if value in faculty_grade:
            self.__position = value
        else:
            raise ValueError(f'Wrong faculty grade: {value}')

    @property
    def specialization(self):
        return self.__specialization

    @specialization.setter
    def specialization(self, value):
        specialization_list = {"Chemistry", "Biology", "Physics", "Business Studies", "Mathematics"}
        if value in specialization_list:
            self.__specialization = value
        else:
            raise ValueError(f'Wrong specialization: {value}')

    def __make_syllabus(self):
        if self.specialization == "Chemistry" and self.position != "senior lecture":
            self.__syllabus = ["Organic chemistry", "Inorganic chemistry"]
        elif self.specialization == "Biology" and self.position != "senior lecture":
            self.__syllabus = ["Biochemistry and cell biology", "Neurobiology"]
        elif self.specialization == "Physics":
            self.__syllabus = ["Physics of soft matter", "Physical chemistry", "Biophysics"]
        elif self.specialization == "Business Studies":
            self.__syllabus = ["Economic and Business statistics", "Economic Principles"]
        elif self.specialization == "Mathematics":
            self.__syllabus = ["Geometry in Physics", "Mathematical relativity", "Mathematical Statistical Physics"]
        else:
            self.__syllabus = ["Structural biology", "Materials and interfaces"]
        return self.__syllabus

    def __make_university_email(self):
        self.email = f'{self.name}.{self.surname}@university.com'.lower()
        return self.email
    def get_data(self):
        return f' Name: {self.name}\n Surname: {self.surname}\n E-mail: {self.__make_university_email()}\n Syllabus: {self.__make_syllabus()}'



class Student(Person):
    def __init__(self, name, surname, course, specialty):
        super().__init__(name, surname)
        self.course = course
        self.speciality = specialty
        self.endroll_subjects = []
        self.grades = {}

@property
def course(self):
    return self.__course

@course.setter
def course(self, value):
    if 0 > value <= 4:
        self.__course = value
    else:
        raise ValueError(f'Wrong course grade {value}')

@property
def specialty(self):
    return self.__specialty

@specialty.setter
def specialty(self, value):
    specialty_list = {"Chemistry", "Biology", "Physics", "Business Studies", "Mathematics"}
    if value in specialty_list:
        self.__specialty = value
    else:
        raise ValueError (f'Wrong specialty {value}')

#список предметов
def enroll(self, subject):
    subject.add_student(self) #тут нужно это написать класс сабжектс и добавить туда метод на который мы тут сошлемся

#оценки по предметам

#средняя оценка

#сдал не сдал (сравнение)

#вывод данных об ученике

class Subjects:
    def __init__(self, title):
        self.title = title
        self.teacher = None
        self.students = []
    
    @property
    def title(self):
        return self.__title
    
    @title.setter
    def title(self, value):
        subjects_and_speality = {
            "Organic chemistry": "Chemistry",
            "Inorganic chemistry": "Chemistry",
            "Materials and interfaces": "Chemistry",
            "Biochemistry and cell biology": "Biology",
            "Neurobiology": "Biology",
            "Structural biology": "Biology",
            "Physics of soft matter": "Physics",
            "Physical chemistry": "Physics",
            "Biophysics": "Physics",
            "Economic and Business statistics": "Business Studies",
            "Economic Principles": "Business Studies",
            "Geometry in Physics": "Mathematics",
            "Mathematical relativity": "Mathematics", 
            "Mathematical Statistical Physics": "Mathematics"
        }
        if value in subjects_and_speality:
            self.__title = value
        else:
            raise ValueError(f'Wrong subjects titile {value}')
    
    def add_speciality(self):
        subjects_and_speality = {
            "Organic chemistry": "Chemistry",
            "Inorganic chemistry": "Chemistry",
            "Materials and interfaces": "Chemistry",
            "Biochemistry and cell biology": "Biology",
            "Neurobiology": "Biology",
            "Structural biology": "Biology",
            "Physics of soft matter": "Physics",
            "Physical chemistry": "Physics",
            "Biophysics": "Physics",
            "Economic and Business statistics": "Business Studies",
            "Economic Principles": "Business Studies",
            "Geometry in Physics": "Mathematics",
            "Mathematical relativity": "Mathematics", 
            "Mathematical Statistical Physics": "Mathematics"
        }
        self.specialty = subjects_and_speality.get(self.title, 'The subjects is ot include in specialties')
        return self.specialty
        

    def add_teacher(self, teacher):
        if isinstance(teacher, Teacher):
            self.teacher = teacher
        else: 
            raise ValueError(f'Wrong class of {teacher}')

    def add_student(self, student):
        if student not in self.students:
            self.students.append(student)
            student.grades.setdefault(self, [])

    def __str__(self):
        teacher = self.teacher.name if self.teacher else 'None'
        return f' Subject: {self.title}\n Specialty: {self.add_speciality()}\n Teacher: {teacher}\n Students: {len(self.students)}'


tc1 = Teacher("Bob", "Dilan", "professor", "Chemistry")
print(tc1.get_data())

print ()
tc2 = Teacher("Tom", "Brown", "associate proressor", "Biology")
print(tc2.get_data())

print()
sb1 = Subjects('Mathematical relativity')
sb1.add_teacher(tc2)
print(sb1)

