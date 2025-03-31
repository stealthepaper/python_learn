# products = 'apple, eggs, milk, orange, bread, caviar, banana, bear, grape, cream'
# products = products.split(', ')
# sum_res = 0
# for i in products:
#     elem_len = len(i)
#     print(f'Длинна слова {i} = {elem_len}')
#     sum_res += elem_len
# print(f'Общая длинна слов = {sum_res}')


# products = 'apple, eggs, milk, orange, bread, caviar, banana, bear, grape, cream'
# products = products.split(', ')
# more_four = []
# less_four = []
# for i in products:
#     if len(i) <= 4:
#         print(f'Длинна слова {i} <= 4')
#         less_four.append(i)
#     else:
#         print(f'Длинна слова {i} > 4')
#         more_four.append(i)

# products = 'apple, eggs, milk, orange, bread, caviar, banana, bear, grape, cream, chicken, wine, cheese, vinegar'
# products = products.split(', ')
# file_names = []
# for i in products:
#     if len(i) < 5:
#         i += '.csv'
#         file_names.append(i)
#     else:
#         i += '.xlsx'
#         file_names.append(i)
# xlsx_file = []
# csv_file = []
# for file in file_names:
#     if 'xlsx' in file_names:
#         xlsx_file.append(file)
#     else:
#         csv_file.append(file)
#     print(f'Файл {file} успешно прочитан')

# my_list = []
# for i in range(1, 22, 2):
#     i = i**2
#     my_list.append(i)
# print(my_list)

# products = 'apple, eggs, milk, orange, bread, caviar, banana, bear, grape, cream, chicken, wine, cheese, vinegar'
# products = products.split(', ')
# for i in range(len(products)):
#     print(i, products[i])


# products = 'apple, eggs, milk, orange, bread, caviar, banana, bear, grape, cream, chicken, wine, cheese, vinegar'
# products = products.split(', ')
# for ind, obj in enumerate(products):
#     print(ind, obj)

# products_dir = {"apple": 3, "eggs": 2, "milk": 4, "bread": 6, "banana": 8, "grape": 13, "cream": 5}
# for i in products_dir.items():
#     print(i)

# from random import randint
# s = 0
# for i in range(7):
#     a = randint(1,100)
#     s += a
#     print(a, end=' ')
# print()
# print(f'Сумма значений {s}')

# n = int(input())
# s = 0
# for i in range(n):
#     a = int(input())
#     s += a
#     print('current s:', s)
# print('total', s)

# n = int(input())
# for i in range (n, 0, -1):
#     print(i)

# quote = input("Введите фразу: ")
# n = int(input("Введите числа: "))
# for i in range(n):
#     print(quote)

# a = int(input())
# b = int(input())
# for i in range(a, b+1):
#     if i%3 ==0 and i%5==0:
#         print('FizzBuzz')
#     elif i%3 ==0:
#         print('Fizz')
#     elif i%5 == 0:
#         print('Buzz')
#     else:
#         print(i)

# a = int(input())
# b = int(input())
# s = 0
# for i in range(a, b+1):
#     s = i**2
#     print(f"Число {i}; его квадрат = {s}; его куб = {s*i}")

# a = int(input())
# sum = 0
# for i in range(1, a):
#     if i%3== 0 or i%5==0:
#         sum += i
# print(sum)

# фигура из звездочек 
# a = int(input())
# for i in range(1, a+1):
#     print('*' * i)
# for i in range(a-1, 0, -1):
#     print('*' * i)

# сумма куюо от 50 до 100 включительно
# a = 0 
# summ = 0 # скорее всего можно обойтись без двух переменных и просто просуммировать внутри цикла sum
# for i in range(50, 101):
#     a = i*i*i
#     summ += a
# print(f'сумма {summ}')

# фактариал числа 
# n = int(input())
# a = 1
# for i in range(1, n+1):
#     a *= i
# print(a)

