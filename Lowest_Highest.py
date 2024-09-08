# Sorting a list of numbers from lowest to highest (and vice versa)

list = [1,23,4,5,236,63,573,57,56]
list.sort()
less_more = list
more_less = list[::-1]
print(f"List ordered from lowest to highest: {less_more}")
print(f"List ordered from highest to lower: {more_less}")