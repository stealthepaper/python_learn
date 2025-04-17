from string import ascii_lowercase
ascii_lowercase = list(ascii_lowercase)
alp_dict = {}
for i in range(len(ascii_lowercase)):
    alp_dict[ascii_lowercase] = i
print(alp_dict)