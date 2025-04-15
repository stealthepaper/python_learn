strings = ["hello", "world", "madam", "python"]
# result = []
# for i in strings:
#     reversed_strings = i[::-1]
#     if i == reversed_strings:
#         result.append(i)
#     else: 
#         result.append((i,reversed_strings))
# print(result)
print([(i, i[::-1]) if i != i[::-1] else i for i in strings])
