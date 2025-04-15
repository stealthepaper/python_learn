def generate_fizz_buzz_list(n):
    # n_list = []
    # for i in range(1,n+1):
    #     if i%3 == 0 and i%5 ==0:
    #         n_list.append('FizzBuzz')
    #     elif i%3 == 0:
    #         n_list.append('Fizz')
    #     elif i%5 == 0:
    #         n_list.append('Buzz')
    #     else:
    #         n_list.append(i)
    # return n_list

    
    n_list = ['FizzBuzz' if i%15 == 0 else 'Fizz' if i%3 == 0 else 'Buzz' if i%5 == 0  else i for i in range(1,n+1)]
    return n_list

print(generate_fizz_buzz_list(4))
# print(generate_fizz_buzz_list(10))
# print(generate_fizz_buzz_list(30))
# print(generate_fizz_buzz_list(40))
