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


products = 'apple, eggs, milk, orange, bread, caviar, banana, bear, grape, cream, chicken, wine, cheese, vinegar'
products = products.split(', ')
for ind, obj in enumerate(products):
    print(ind, obj)

products_dir = {"apple": 3, "eggs": 2, "milk": 4, "bread": 6, "banana": 8, "grape": 13, "cream": 5}
for i in products_dir.items():
    print(i)