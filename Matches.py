# Contar las matches en un texto

text = input("Enter text: ")
word = input("Enter text to search: ")
matches = text.count(word)

if matches > 0: print(f'"{word}" was found {matches} times in the text.')
else: print("No matches founds")