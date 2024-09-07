# area de un rectangulo xdxd
while True:
    try: lenght = float(input("Enter the lenght in cm: "))
    except: print("Enter a number as a lenght")
    else: break
while True:   
    try: width = float(input("Enter the height in cm: "))
    except: print("Enter a number as a width")
    else: break

print(f"The area of the rectangle is: {lenght*width}cm²")