# вводится один символ — строчная буква, затем вводится предложение. вывыести все слова с символом
letter = input()
sentance = list(input().split())
for i in range(len(sentance)):
    if (letter in sentance[i]) or (letter.upper() in sentance[i]):
        print(sentance[i])