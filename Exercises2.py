# Exercise 1
# name = input("Enter your name: ")
# print(f"{name.upper()} has {len(name)} letters")

# Exercise 2
# phrase = input("Write any phrase: ")
# reversed_phrase = phrase[::-1]
# print(reversed_phrase)

# Exercise 3
# email = input("Enter your email: ")
# print(email[:email.find('@')] + '@ceu.es')

# Exercise 4
# shopping = input("Enter your shopping list (items separated by commas): ")
# print(shopping.replace(',', '\n'))

# Exercise 5
# product = input("Product name: ")
# price = float(input("Product price: "))
# units = int(input("Number of units: "))
# print(f"{product.capitalize()} : {units} units x ${round(price,2)} = ${round(price*units,2)}")

# Exercise 6
# age = int(input("Enter your age: "))
# if age >= 18:
#     print("You are an adult.")
# elif age < 18:
#     print("You are a minor.")

# Exercise 7
# password = "hola123xd"
# verify = input("Enter the password: ")
# if password == verify.lower():
#     print("Both passwords match")
# else:
#     print("The passwords do not match")

#--------Syntax and Data Structures---------

# Exercise 8
# numbers = [1,2,3,4,5,6,7,8,9,10]
# even_numbers = []
# for n in numbers:
#     if n % 2 == 0:
#         even_numbers.append(n)
#     else:
#         continue
# print(even_numbers)
# Completed! Very quick and easy even with little programming experience

# Exercise 9
# ages = {
#     "Juan": 18,
#     "Carlos": 16,
#     "Santiago": 17,
#     "Angel": 21
# }
#
# for name, age in ages.items():
#     if age >= 18:
#         print(name)
# Completed! I just had to "remember" (gpt) list methods and their use

# Exercise 10
# words_set = {"palabra", "sol", "ola", "si", "palta", "amor"}
# short_words = {""}
# for w in words_set:
#     if len(w) <= 4:
#         short_words.add(w)
# short_words.remove("")
# print(short_words)
# Completed! It was a bit tricky but it worked

# Exercise 11
# products = [("iphone 15 pro", 1000), ("PC Gamer", 850), ("chocolate", 1)]  # prices in USD
#
# def most_expensive_product(product_list):
#     prices = []
#     for p in product_list:
#         prices.append(p[1])
#     return max(product_list, key=lambda t: t[1])[0], max(prices)
#
# print(most_expensive_product(products))
# Completed! but I used gpt to remember the product name handling

# Exercise 12
words_list = ["hi", "sun", "hi", "sun", "sun", "sugar", "melon"]
counts = {}

for word in words_list:
    if word in counts:
        counts[word] += 1
    else:
        counts[word] = 1

print(counts)
# Completed!