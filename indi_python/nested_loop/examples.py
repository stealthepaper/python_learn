# # пример со столиком
# tables = ['A01', 'B02']
# for table in tables:
#     print(f'Начинаем обслуживание столика {table}')
#     for person in range(4):
#         print(f'Официант подал блюдо к столу {table} человеку {person}')
# print(f'Стол {table} полностью обслужен')


# # пример с '*'
# for i in range(3):
#     for j in range(5):
#         print('*', end=" ")
#     print()

# for i in range(3):
#     for j in range(5):
#         print(i, end=" ")
#     print()

# вывод внутренней и внешней переменной
# for i in range(2):
#     for j in range(3):
#         print(f'i = {i}, j = {j};', end = " ")
#     print()

# # зависмимость переменных
# for i in range(1, 6):
#     for j in range(i):
#         print(f'i = {i} j = {j};', end=' ')
#     print()

# перебор всех пар
fruits = ['apple', 'banana', 'orange' ]
for i in fruits:
    for j in range(1, 21, 5):
        print(f'sale for {i} = {j}%')
