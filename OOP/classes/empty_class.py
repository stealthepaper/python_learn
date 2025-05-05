class Empty:
    pass       


my_list = [
    ('apple', 23),
    ('banana', 80),
    ('cherry', 13),
    ('date', 10),
    ('elderberry', 4),
    ('fig', 65),
    ('grape', 5),
    ('honeydew', 7),
    ('kiwi', 1),
    ('lemon', 10),
]

my_list = [setattr(Empty, f'{i[0]}', i[1]) for i in my_list]

print(Empty.__dict__)