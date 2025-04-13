def print_initials(name, surname, middlename):
    print(f'{surname.title()} {name[:1].title()}.{middlename[:1].title()}.')

print_initials('Мария', 'Иванова', 'Филлиповна')
print()
print_initials('евгЕний', 'петросян', 'ВаГАнович')