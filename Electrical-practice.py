# Hours left to finish my Electrical Professional Practice
import json
import os

hours = 360

# Schedule Monday-Thursday (hours per day)
sch_mon_thu = 10
# Schedule on Fridays (hours per day)
sch_fri = 8

JSON_PATH = os.path.join(os.path.dirname(__file__), "tp-hours.json")

def _ensure_json():
    if not os.path.exists(JSON_PATH):
        default = {"Mon-Thu-Days": 0, "Fri-Days": 0}
        with open(JSON_PATH, "w", encoding="utf-8") as f:
            json.dump(default, f, ensure_ascii=False, indent=2)

def total_hours():
    return hours

def current_hours():
    _ensure_json()
    with open(JSON_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)
    mon_thu = int(data.get("Mon-Thu-Days", 0))
    fri = int(data.get("Fri-Days", 0))
    return mon_thu * sch_mon_thu + fri * sch_fri

def hours_left():
    return total_hours() - current_hours()

def _read_data():
    _ensure_json()
    with open(JSON_PATH, "r", encoding="utf-8") as f:
        return json.load(f)

def _write_data(data):
    with open(JSON_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def add_day():
    try:
        schedule = int(input("Press '1' for Mon-Thu sch or press '2' for Fri sch: "))
    except ValueError:
        return "Invalid selection."

    data = _read_data()

    if schedule == 1:
        print("Current Days =", data.get("Mon-Thu-Days", 0))
        try:
            days_added = int(input("Enter the number of days to add in Mon-Thu sch (integer): "))
        except ValueError:
            return "Invalid number."
        data["Mon-Thu-Days"] = data.get("Mon-Thu-Days", 0) + days_added
        _write_data(data)
        return f"Days Added = {days_added}\nCurrent Days on Mon-Thu = {data['Mon-Thu-Days']}"

    elif schedule == 2:
        print("Current Days =", data.get("Fri-Days", 0))
        try:
            days_added = int(input("Enter the number of days to add in Fridays sch (integer): "))
        except ValueError:
            return "Invalid number."
        data["Fri-Days"] = data.get("Fri-Days", 0) + days_added
        _write_data(data)
        return f"Days Added = {days_added}\nCurrent Days on Fridays = {data['Fri-Days']}"

    else:
        return "Option not available"

def modify_day():
    try:
        schedule = int(input("Press '1' for Mon-Thu sch or press '2' for Fri sch: "))
    except ValueError:
        return "Invalid selection."

    data = _read_data()

    if schedule == 1:
        print("Current Days = ", data.get("Mon-Thu-Days", 0))
        try:
            new_day = int(input("Set the new day (integer >= 0): "))
            if new_day < 0:
                return "Day must be non-negative."
        except ValueError:
            return "Invalid number."
        data["Mon-Thu-Days"] = new_day
        _write_data(data)
        return f"{data['Mon-Thu-Days']} is the new day value of Mon-Thu sch."

    elif schedule == 2:
        print("Current Days =", data.get("Fri-Days", 0))
        try:
            new_day = int(input("Set the new day (integer >= 0): "))
            if new_day < 0:
                return "Day must be non-negative."
        except ValueError:
            return "Invalid number."
        data["Fri-Days"] = new_day
        _write_data(data)
        return f"{data['Fri-Days']} is the new day value of Fri-Days sch."
    else:
        return "Option not available"

def view_json():
    data = _read_data()
    return f"Mon-Thu-Days = {data.get('Mon-Thu-Days', 0)}\nFri-Days = {data.get('Fri-Days', 0)}"

def main():
    print("""
These are the options to view about the TP hours practice:

    1) Total Hours
    2) Current Hours
    3) Hours Left
    4) Add Day
    5) Modify Day
    6) View Json file

    0) Exit
""")
    try:
        option = int(input("Select an option by a number: "))
    except ValueError:
        print("Please enter a number.")
        return

    if option == 0:
        print("Bye!")
        exit()
    elif option == 1:
        print("Total Hours =", total_hours())
    elif option == 2:
        print("Current Hours =", current_hours())
    elif option == 3:
        print(f"Hours Left = {hours_left()}")
    elif option == 4:
        print(add_day())
    elif option == 5:
        print(modify_day())
    elif option == 6:
        print(view_json())
    else:
        print("Option not available")

if __name__ == "__main__":
    while True:
        main()
        
