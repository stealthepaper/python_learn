# Найдите, в каких строках из введённых и в каком месте упоминается «рок», причем регистр букв не важен.
# Вместо явного цикла прохода по строке в цикле используйте подходящий метод строки.
# Формат ввода
# На первой строке вводится натуральное число N — количество строк.
# Далее следуют N строк.

# первый вариант, работает. но тупо как-то
n = int(input())
index = 0
for i in range(n):
    qt = input().lower()
    index = qt.find('рок')
    if 'рок' in qt:
        print(i, index+1)

#  дурка с энумирейт 
n = int(input())
qt_dic =  []
world = 'рок'
for i in range(n):
    qt = input().lower()
    qt_dic.append(qt)
for l, s in enumerate(qt_dic, start=1):
    if world in s:
        print(l, s.index(world)+1)
