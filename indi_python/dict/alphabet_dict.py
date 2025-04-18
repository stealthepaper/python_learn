from string import ascii_lowercase
alphabet = {}
c = 0
for i in ascii_lowercase:
    c += 1
    for j in range(len(ascii_lowercase)):
        alphabet[i] = c
print(alphabet)