def check_password(psswd):
    count_digit = 0
    count_upper = 0
    count_spe = 0
    for s in psswd:
        if s.isdigit():
            count_digit +=1
    for i in psswd:
        if i.isupper():
            count_upper += 1
    for n in psswd:
        if n in "!@#$%*":
            count_spe += 1
    # print(count_upper, count_digit, count_spe)
    if len(psswd) >= 10 and count_digit >= 3 and count_upper >= 1 and count_spe >= 1:
        print('Perfect password')
    else:
        print('Easy peasy')


check_password('12345!!8')
print()
check_password('Qwerty1357!')
print()
check_password('Qwerty1357)')