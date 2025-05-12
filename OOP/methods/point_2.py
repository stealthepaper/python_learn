class Point:
    def set_coordinates(self, value_1, value_2):
        self.x = value_1
        self.y = value_2
    def get_distance_to_origin(self):
        if hasattr(self, 'x') and hasattr(self, 'y'):
            self.distance = (self.x**2 + self.y**2)**0.5
            return self.distance
        else: 
            return
    def display(self):
        if hasattr(self, 'x') and hasattr(self, 'y'):
            print(f'Point({self.x}, {self.y})')
        else:
            print('Координаты не заданы')
    def get_distance(self, objct):
        if  isinstance(objct, Point) == True :
            if hasattr(objct, 'x') and hasattr(objct, 'y'):
                d = ((self.x - objct.x)**2 + (self.y - objct.y)**2)**0.5
                return d
            else:
                print('Координаты не заданы')
                return
        else:
            print('Передана не точка')
            return

p1 = Point()
p1.set_coordinates(1, 2)
print(p1.get_distance(100))
print(p1.get_distance([1, 2, 3]))
print(p1.get_distance(Point()))

print()

p1 = Point()
p2 = Point()
p1.set_coordinates(1, 2)
p2.set_coordinates(4, 6)
p1.display()
p2.display()
print(p1.get_distance(p2))
print(p2.get_distance(p1))

print()

p1 = Point()
p2 = Point()
print(p1.get_distance(p2))
p1.set_coordinates(1, 2)
print(p1.get_distance(p2))
p2.set_coordinates(4, 6)
print(p1.get_distance(p2))