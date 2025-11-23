# Isogram: a word with no repeated letters
# Goal: read a word from input and print True/False
# An empty string is an isogram
# Function is case-insensitive (A and a treated the same)
# If there is more than one word return False
# No accented letters are expected

word = input("Enter a word: ").strip().lower()

def is_single_word(s):
    return " " not in s

def contains_digit(s):
    return any(ch.isdigit() for ch in s)

def is_isogram(s):
    return len(set(s)) == len(s)

def verify(s):
    if s == "":
        return True
    return is_single_word(s) and not contains_digit(s) and is_isogram(s)

print(verify(word))