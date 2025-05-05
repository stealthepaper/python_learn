class Person:
    name = "John Smith"
    age = 30
    gender = "male"
    address = "123 Main St"
    phone_number = "555-555-5555"
    email = "johnsmith@example.com"
    is_employed = True


words_att = input().split()
for one_word in words_att:
    if hasattr(Person, one_word.lower()) == True:
        print(f'{one_word} - YES')
    else:
        print(f'{one_word} - NO')