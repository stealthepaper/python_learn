# person = dict(name = 'Vasay', surname = 'Petrov', age = 25)
# print(person)

# sweet = {
#     "id": "0001",
#     "type": "donut",
#     "name": "Cake",
#     "ppu": 0.55,
#     "calories": 125,
# }
# print(sweet['name'])
# print(sweet['calories'])
# print(sweet['id'])


# days = {
#     1: 31,
#     2: 28,
#     3: 31,
#     4: 30,
#     5: 31,
#     6: 30,
#     7: 31,
#     8: 31,
#     9: 30,
#     10: 31,
#     11: 30,
#     12: 31
# }

# n = int(input())
# print(days[n])

sweet = {
    "id": "0001",
    "type": "donut",
    "name": "Cake",
    "ppu": 0.55,
    "calories": 125,
}

sweet['weight'] = 230
sweet['have_topping'] = True
sweet['name'] = 'SuperCake'
sweet['calories'] = 350
del(sweet['ppu'])
del(sweet['type'])
print(sweet)