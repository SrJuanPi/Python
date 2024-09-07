# Calculator of how many decades and years a person has

while True:
    try: age = int(input("Enter your age: "))
    except: print("Please enter a number")
    else: break
decades = age // 10
years = age % 10

print(f"You are {decades} decades and {years} years old.")