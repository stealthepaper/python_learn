class Point:
    def __init__(self, coord_x = 0, coord_y = 0):
        self.move_to(coord_x, coord_y)

    def move_to(self, new_x, new_y):
        self.x = new_x
        self.y = new_y

    def go_home(self):
        self.move_to(0, 0)

    def print_point(self):
        return f'Координаты точки x: {self.x}, y: {self.y}'

    def get_distance(self, another_point):
        if not isinstance(another_point, Point):
             raise ValueError('Аргумент должен принадлежать классу Point')
        else:
            return ((self.x - another_point.x)**2 + (self.y - another_point.y)**2)**0.5


point1 = Point(3, 4)
point1.move_to(6,7)
point1.go_home
point1.move_to(2, 1)
print(point1.print_point())

p2 = Point(2, 4)
p2.get_distance(5) 

class Point_2:
    def set_coordinates(self, x, y):
        self.x = x
        self.y = y
    
    def check_exist_coord(self) -> bool:
        return hasattr(self, 'x') and hasattr(self, 'y')

    def get_distance_to_origin(self):
        if self.check_exist_coord():
            return (self.x ** 2 + self.y ** 2) ** 0.5
        return None

    def get_distance(self, point2):
        if not isinstance(point2, Point_2):
            print('Передана не точка')
            return None
        if self.check_exist_coord() and point2.check_exist_coord():
            return (abs(self.x - point2.x) ** 2 + abs(self.y - point2.y) ** 2) ** 0.5
        print('Координаты не заданы')
        return None

    def display(self):
        if self.check_exist_coord():
            print(f"Point({self.x}, {self.y})")
        else:
            print('Координаты не заданы')

p1 = Point_2()
p1.set_coordinates(1, 2)
print(p1.get_distance(100))
print(p1.get_distance([1, 2, 3]))

print()

