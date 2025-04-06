# Создайте список первых букв каждого слова строки, в переменной phrase, и выведите его


# phrase = 'Create a list of the first letters of every word in this string'
# phrase = "Hello world this is Python"
# phrase = "Machine Learning and AI"
phrase = "Single"
phrase = phrase.split()
phrase_list = [i[0:1] for i in (phrase)]
print(phrase_list)