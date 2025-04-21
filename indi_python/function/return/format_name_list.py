def format_name_list (names: list) -> str:
    names_values = []
    for dic in (names):
        names_values.append(dic.get('name'))
    names_values_str = ", ".join(names_values)
    return (names_values_str)

print(format_name_list([{'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'}])) #  'Bart, Lisa и Maggie'
# format_name_list([{'name': 'Bart'}, {'name': 'Lisa'}]) #'Bart и Lisa'
# format_name_list([{'name': 'Bart'}])
# format_name_list([])
print(format_name_list([{'name': 'Maggie'}, {'name': 'Lisa'}, {'name': 'Barney'}, {'name': 'Homer'}, {'name': 'Bart'}, {'name': 'Moe'}]))