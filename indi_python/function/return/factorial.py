def factorial(x):
    prn = 1
    for i in range(1, x+1):
        prn *= i
    return prn

print(factorial(4))
print(factorial(5))
print(factorial(1))
print(factorial(0))
print(factorial(11))
print(factorial(17))
