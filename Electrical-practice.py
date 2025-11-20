# Hours left to finish my Electrical Professional Practice
import json

hours = 360

# Schedule Monday to Thuesday, in hours, per day
sch_mon_thu = 10
# Schedule on Fridays, in hours
sch_fri = 8

def total_hours():
    return hours

def current_hours():
    with open("tp-hours.json", "r", encoding="utf-8") as f:
        data = json.load(f) # devuelve dict o list

    current_hours = data["Mon-Thu-Days"]*sch_mon_thu + data["Fri-Days"]*sch_fri
    return current_hours
    
def hours_left():
    with open("tp-hours.json", "r", encoding="utf-8") as f:
        data = json.load(f)
        
    hours_left = hours - current_hours()
    
    return f"Hours Left = {hours_left}"

def add_day():
    schedule = int(input("Press '1' for Mon-Thu sch or press '2' for Fri sch: "))
    
    if schedule == 1:
        with open("tp-hours.json", "r", encoding="utf-8") as f:
            data = json.load(f) 
        
        print("Current Days =", data["Mon-Thu-Days"])
        days_added =  int(input("Enter the number of days to add in Mon-Thu sch (integer): "))
        data["Mon-Thu-Days"] += days_added
        
        with open("tp-hours.json", "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
            
        return f"Days Added = {days_added}\nActual Days = {data["Mon-Thu-Days"]}"
        
    elif schedule == 2:
        with open("tp-hours.json", "r", encoding="utf-8") as f:
            data = json.load(f)
            
        print("Current Days =", data["Fri-Days"])
        days_added =  int(input("Enter the number of days to add in Fridays sch (integer): "))
        data["Fri-Days"] += days_added
        
        with open("tp-hours.json", "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
            
        return f"Days Added = {days_added}\nCurrent Days = {data["Fri-Days"]}"
        
    else:
        print("Option not available")

def modify_day():
    schedule = int(input("Press '1' for Mon-Thu sch or press '2' for Fri sch: "))
    
    if schedule == 1:
        with open("tp-hours.json", "r", encoding="utf-8") as f:
            data = json.load(f)
            
        print("Current Days = ", data["Mon-Thu-Days"])
        new_day = int(input("Set the new day: "))
        data["Mon-Thu-Days"] = new_day
        
        with open("tp-hours.json", "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        
        return f"{data["Mon-Thu-Days"]} is the new day value of Mon-Thu sch."
        
    elif schedule == 2:
        with open("tp-hours.json", "r", encoding="utf-8") as f:
            data = json.load(f)
            
        print("Current Days =", data["Fri-Days"])
        new_day = int(input("Set the new day: "))
        data["Fri-Days"] = new_day
        
        with open("tp-hours.json", "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        
        return f"{data["Fri-Days"]} is the new day value of Fri-Days sch."
    else:
        print("Option not available") 
        
def view_json():
    with open("tp-hours.json", "r", encoding="utf-8") as f:
        data = json.load(f)
        
    return f"Mon-Thu-Days = {data["Mon-Thu-Days"]}\nFri-Days = {data["Fri-Days"]}"

def main():
    print("""
These are the options to view about the TP hours practice:

    1) Total Hours
    2) Current Hours
    3) Hours Left
    4) Add Day
    5) Modify Day
    
    0) Exit
""")
    
    option = int(input("Select an option by a number: "))
    
    if option == 0: 
        print("Bye!")
        exit()
    elif option == 1: print("Total Hours =", total_hours())
    elif option == 2: print("Current Hours =", current_hours())
    elif option == 3: print(hours_left()) 
    elif option == 4: print(add_day())
    elif option == 5: print(modify_day())
    else:
        print("Option not available")

if __name__ == "__main__":
    while True:
        main()