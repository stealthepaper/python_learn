a, b = map(int, input().split())
if a <= b:
    n = [i**2 for i in range(a,b+1)]
    print(n)
else:
    m = [i**3 for i in range(a, b-1, -1)]
    print(m)