def summ_n(t):
    S = 0
    for i in range(t+1):
        S += i
    print(f'Я знаю, что сумма чисел от 1 до {t} равна {S}')

summ_n(2)
summ_n(3)
summ_n(5)