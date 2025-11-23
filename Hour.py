# Create a program that converts hours to minutes, and vice versa (if I can)
import re

while True:
    time_input = input("Enter the time in hours or minutes: ")
    hour_format = r"\d{1,}:\d{1,2}"
    minute_format = r"\d{1,}"
    match_hour = re.match(hour_format, time_input)
    match_minute = re.match(minute_format, time_input)
    
    if match_hour:
        parts = time_input.split(":")
        if len(parts) > 2:
            print("Invalid time format. Allowed format is 'hours:minutes'.")
            continue
            
        hour = int(parts[0])
        minutes = int(parts[1])
        
        if minutes > 59:
            print("Invalid time format. Minutes cannot be greater than 59.")
            continue
        
        total_minutes = hour * 60 + minutes
        print(f"{hour}h {minutes}m is {total_minutes} minutes.")
        break
    
    elif match_minute:
        try:
            minutes = int(time_input)
        except:
            print("Invalid time format. If using hours, make sure to include minutes.")
            continue
        hours = minutes / 60
        decimal = hours - int(hours)
        new_minutes = int(decimal * 60)
        if new_minutes < 10:
            new_minutes = f"0{str(new_minutes)}"
        print(f"{minutes} minutes is {round(hours,2)} hours or {int(hours)}:{new_minutes}.")
        break
    
    else:
        print("Invalid format. Use 'hours:minutes' or just minutes.")
        continue