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

products = 'apple, eggs, milk, orange, bread, caviar, banana, bear, grape, cream, chicken, wine, cheese, vinegar'
products = products.split(', ')
file_names = []
for i in products:
    if len(i) < 5:
        i += '.csv'
        file_names.append(i)
    else:
        i += '.xlsx'
        file_names.append(i)
print(file_names)
xlsx_file = []
csv_file = []
for file in file_names:
    if 'xlsx' in file_names:
        xlsx_file.append(file)
    else:
        csv_file.append(file)
    print(f'Файл {file} успешно прочитан')