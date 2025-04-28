def factorial(n) -> int:
    r_factorial = 1
    for i in range(2, n+1):
        r_factorial *= i
    return r_factorial

def trailing_zeros(x) -> int:
    s = str(factorial(x))[::-1]
    zeros = 0 
    for num in s:
        if num == '0':
            zeros +=1
        else:
             return zeros


print(trailing_zeros(6))
print(trailing_zeros(0))
print(trailing_zeros(30))
print(trailing_zeros(12))
print(trailing_zeros(10))
print(trailing_zeros(20))