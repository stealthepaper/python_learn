class Stack:
    def __init__(self):
        self.values = []

    def push(self, item):
        self.values.append(item)
    
    def pop(self):
        print()

    def peek(self):
            s = self.values.reverse()
            return s
    def is_empty(self):
        return self.values == []
    def size(self):
        return len(self.values)



s = Stack()
# assert s.values == []
# assert isinstance(s, Stack)

# assert s.is_empty() is True
s.push('cat')
# assert s.size() == 1

s.push('dog')
# assert s.size() == 2

s.push(True)
# assert s.size() == 3
# assert s.is_empty() is False

# print('Good')

print(s.peek())