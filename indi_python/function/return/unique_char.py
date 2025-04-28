def first_unique_char(n):
    for i in n:
        if n.count(i)==1:
            return(n.index(i))
    return('-1')

print(first_unique_char('python'))
print(first_unique_char('abracadabra'))
print(first_unique_char('abcabc'))
print(first_unique_char('445644894984512311655648484'))
print(first_unique_char('rewgfdgdgdgdreetetetjhjgkykyuk'))
print(first_unique_char('aasssddddddddq'))