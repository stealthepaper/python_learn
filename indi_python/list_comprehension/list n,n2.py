# создайте список, состоящий из нечетных натуральных чисел в интервале [n,n2]

n = int(input())
n_list = [i for i in range(n,(n**2)+1) if i%2==1]
print(n_list)
