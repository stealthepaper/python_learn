def sum_num(n):
    n = list(n)
    t = 0
    for i in n:
        if i.isdigit():
            i = int(i)
            t += i
    print(t)

sum_num('12')
sum_num('1888')
sum_num('45')
sum_num('123QwertY321')
sum_num('-123.78')


# n = input()
# n = list(n)
# t = 0
# for i in n:
#     if i.isdigit():
#         i = int(i)
#         t += i
# print(t)