def find_duplicate(a):
    duplicates = []
    for i in a:
        if i not in duplicates and a.count(i)  > 1:
            duplicates.append(i)
    return duplicates
            

print(find_duplicate([1, 1, 1, 1, 1, 2, 2, 2, 2]))
print(find_duplicate([2, 1, 1, 1, 1, 1, 2, 2, 2, 2]))
print(find_duplicate([1, 2, 3, 4]))
print(find_duplicate([8, 7, 6, 5, 4, 3, 4, 5, 6, 7, 8]))
