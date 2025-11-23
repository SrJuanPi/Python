# Celsius/Fahrenheit temperature converter

def convert_temperature():
    while True:
        try:
            degrees = float(input("Enter temperature: "))
        except ValueError:
            print("Please enter a valid number.")
        else:
            break

    to_unit = input("Convert to Fahrenheit (F) or Celsius (C): ").strip().lower()

    if to_unit == "f":
        celsius = degrees
        fahrenheit = (celsius * 9/5) + 32
        print(f"{celsius}°C equals {round(fahrenheit, 2)}°F")
    elif to_unit == "c":
        fahrenheit = degrees
        celsius = (fahrenheit - 32) * 5/9
        print(f"{fahrenheit}°F equals {round(celsius, 2)}°C")
    else:
        print("Invalid option.")

convert_temperature()