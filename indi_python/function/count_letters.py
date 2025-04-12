def count_letters(quote):
    K = 0
    N = 0 
    for i in [i for i in quote]:
        if i.isupper():
            N += 1
        elif i.islower():
            K += 1
    print(f'Количество заглавных символов: {N}')
    print(f'Количество строчных символов: {K}')

count_letters('Привет, Старина')
print()
count_letters('QWERTY')
print()
count_letters('abcdrQ')
print()
count_letters('LEO Messi')