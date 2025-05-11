class Point:
    def set_coordinates(self, value_1, value_2):
        self.x = value_1
        self.y = value_2
    def get_distance_to_origin(self):
        try:
            self.distance = (self.x**2 + self.y**2)**0.5
            return self.distance
        except: 
            return
    def display(self):
        try:
            print(f'Point({self.x},{self.y})')
        except:
            print('Координаты не заданы')

# class Point:
#     def set_coordinates(self, value_1, value_2):
#         self.x = value_1
#         self.y = value_2
#     def get_distance_to_origin(self):
#         if hasattr(self, 'x') and hasattr(self, 'y'):
#             self.distance = (self.x**2 + self.y**2)**0.5
#             return self.distance
#         else: 
#             return
#     def display(self):
#         if hasattr(self, 'x') and hasattr(self, 'y'):
#             print(f'Point({self.x}, {self.y})')
#         else:
#             print('Координаты не заданы')

p2 = Point()
p2.display()
p2.set_coordinates(3, 4)
p2.display()
print(p2.get_distance_to_origin())

print()

p3 = Point()
p3.display()
print(p3.get_distance_to_origin())
p3.x = 4
p3.display()
print(p3.get_distance_to_origin())
p3.y = 3
p3.display()
print(p3.get_distance_to_origin())
