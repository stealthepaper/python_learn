def format_name_list (names: list) -> str:
    names_values = []
    for dic in (names):
        names_values.append(dic.get('name'))
    if len(names_values) == 0:
        return ""
    elif len(names_values) == 1:
        return names_values[0]
    else: 
        return f"{', '.join(names_values[:-1])} и {names_values[-1]}"

print(format_name_list([{'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'}])) #  'Bart, Lisa и Maggie'
print(format_name_list([{'name': 'Bart'}, {'name': 'Lisa'}])) #'Bart и Lisa'
print(format_name_list([{'name': 'Bart'}]))
print(format_name_list([]))
print(format_name_list([{'name': 'Marge'},{'name': 'Maggie'},{'name': 'Seymour'}]))
print(format_name_list([{'name': 'Maggie'}, {'name': 'Lisa'}, {'name': 'Barney'}, {'name': 'Homer'}, {'name': 'Bart'}, {'name': 'Moe'}]))