# Calculate the average of a list of numbers

# We import the random library to make it more interesting
import random

list_lenght = random.randrange(5, 100)
number_list = []

# A random number for each item on the list
for i in range(1, list_lenght+1):
    number = random.randrange(i, list_lenght+1)
    number_list.append(number)
    
# Average function
def average(number_list):
    return sum(number_list) / len(number_list)

# Print result in the console
print(f"The list lenght is: {list_lenght}")
print(f"The list elements are: {number_list}")
print(f"The average of numbers is: {average(number_list)}")
