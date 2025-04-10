n = int(input())
for i in range(n):
    for j in range(n):
        if j%2 == i%2:
            print("X", end=" ")
        else:
            print("O", end= " ")
    print()