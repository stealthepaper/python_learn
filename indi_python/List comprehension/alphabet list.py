# При помощи list comprehension создайте список, состоящий из первых n заглавных букв английского алфавита:
from string import ascii_uppercase
n = int(input())
alb_list = [j[i] for i in range(n) for j in ascii_uppercase.split()]
print(alb_list)