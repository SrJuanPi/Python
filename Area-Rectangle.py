# Calculate the area of a rectangle

# Lenght input
while True:
    try: lenght = float(input("Enter the lenght in cm: "))
    except ValueError: print("\nEnter a number as a lenght\n")
    else: break
    
# Height input
while True:   
    try: width = float(input("Enter the height in cm: "))
    except ValueError: print("\nEnter a number as a width\n")
    else: break

# Area Function
def area(l, w):
    return lenght*width

# Print Result
result = area(lenght, width)
print(f"The area of the rectangle is: {result}cm²")
