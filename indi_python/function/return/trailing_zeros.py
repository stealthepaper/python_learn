def trailing_zeros(x):
    prn = 1
    for i in range(1, x+1):
        prn *= i
    str(prn)
    


print(trailing_zeros(6))