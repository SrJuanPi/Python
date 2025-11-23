# Speed calculator

def speed_calculator():
    
    print("Calculate Speed")  # Introduction
    
    while True:  # Repeat until 'm' or 'km' is entered
        
        distance_unit = input("Select the distance unit: Meters (m) or Kilometers (km): ")
        
        if distance_unit.lower() == "km":
            while True:  # Prevent invalid input
                try:
                    distance = float(input("Enter the distance traveled in km: "))
                except:
                    print("Please enter a valid number")
                else:
                    break
            while True:
                try:
                    time = float(input("Enter the total travel time in hours: "))
                except:
                    print("Please enter a valid number")
                else:
                    break
            print()
            
            speed = distance / time
            print(f"The speed is: {round(speed, 2)} km/h")     # Speed formula for hours and seconds
            print(f"Which equals: {round((speed/3.6), 2)} m/s")
            break
        
        elif distance_unit.lower() == "m":
            while True:
                try:
                    distance = float(input("Enter the distance traveled in m: "))
                except:
                    print("Please enter a valid number")
                else:
                    break
            while True:
                try:
                    time = float(input("Enter the total travel time in seconds: "))
                except:
                    print("Please enter a valid number")
                else:
                    break
            print()
            # Same for the other case
            speed = distance / time
            print(f"The speed is: {round(speed, 2)} m/s")
            print(f"Which equals: {round((speed*3.6), 2)} km/h")
            break
        else:
            print("Invalid format, please try again")

speed_calculator()
