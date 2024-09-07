# Get a set of numbers separated by commas and create a list

# Example of the result: set = [4,5,2,4,5,78,892,3,4]

text = input('Enter a set of words or numbers separated by commas: ')
text = text.replace(" ", "")
numbers = text.split(",")
numbers = [i for i in numbers if i != ""] # This line was made with AI
print(numbers)

# Successfully completed
# Note: You can add 2 things. 1-Convert the elements to numbers, and 
# 2-Create a function in case a letter is entered.