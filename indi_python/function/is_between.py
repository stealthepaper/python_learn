def is_between(a,b,c):
    if a in range(b, c+1) or a in range(c, b+1):
        print('True')
    else:
        print('False')

is_between(5, 3, 6)
is_between(10, 2, 5)
is_between(9, 9, 9)
is_between(5, 9, 1)
is_between(1, 2, 4)
is_between(7, 10, 7)
is_between(7, 10, 8)
