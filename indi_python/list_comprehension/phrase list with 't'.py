phrase = "The tiger talks to the turtle"
phrase = phrase.split()
a = [i for i in phrase if i[0] == 'T' or i[0] == 't']
print(a)