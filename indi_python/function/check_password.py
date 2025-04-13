# def check_password(psswd):
#     count_digit = 0
#     count_upper = 0
#     count_spe = 0
#     for s in psswd:
#         if s.isdigit():
#             count_digit +=1
#         elif s.isupper():
#             count_upper += 1
#         elif s in "!@#$%*":
#             count_spe += 1
#     if len(psswd) >= 10 and count_digit >= 3 and count_upper >= 1 and count_spe >= 1:
#         print('Perfect password')
#     else:
#         print('Easy peasy')

def check_password(psswd):
    number = [i for i in psswd if i.isdigit()]
    letter = [i for i in psswd if i.isupper()]
    symbol = [i for i in psswd if i in "!@#$%*"]
    print('Perfect password' if len(number)>= 3 and len(letter) >= 1 and len(symbol) >= 1 and len(psswd) >= 10 else 'Easy peasy')


check_password('12345!!8') # ep
print()
check_password('Qwerty1357!') # pp
print()
check_password('Qwerty1357)') # ep
print()
check_password('Qwerty17!') # ep
print()
check_password('Qwerty137$') # pp