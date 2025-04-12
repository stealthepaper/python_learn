n = int(input())
n2 = [i for i in range(n, (n**2)+1) if i%2 == 1]
print(tuple(n2))