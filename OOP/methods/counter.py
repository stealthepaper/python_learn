class Counter:
    def start_from(self, value = 0):
        self.value = value
    def increment(self):
        self.value += 1
    def display(self):
        print(f'Текущее значение счетчика = {self.value}')
    def reset(self):
        self.value = 0

c1 = Counter()
c2 = Counter()
c1.start_from(10)
c2.start_from(20)
c1.increment()
c2.increment()
c1.display()
c2.display()
c1.reset()
c1.display()
c2.display()