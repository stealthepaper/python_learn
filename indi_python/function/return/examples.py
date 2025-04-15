# tyt None tk func nichego ne vosvrashaet
def sqr_1 (a, b):
    a**b

resualt = sqr_1(2, 2)
print(f'res = {resualt}')

# tyt ect return i vse good
def sqr_2(c, d):
    return(c**d)

res = sqr_2(3,3)
print(f'res = {res}')

#chetnoe i nechetnoe
def is_even(x):
    if x%2==0:
        return('True') 
    return("False")

for i in range(1,11):
    print(f'{i} - {is_even(i)}')