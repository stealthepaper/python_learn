# В вашем распоряжении имеется список names.
# На основании его при помощи генератора списков создайте новый список, по шаблону
# My name is <имя>

names = ['Alice', 'Bob', 'Marry', 'Joe', 'Hilary', 'Stevia', 'Dylan', 'Kevin', 'Darvin']
my_name_list = [f'My name is {i}' for i in names]
print(my_name_list)