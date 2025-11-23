import re
# for birthday in range(1, 367):
#     if birthday == 163:                   original idea
#         print("Happy Birthday!")

def is_leap_year(year):  #  Improvemet made wiht gpt-4
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
def days_per_month(month, leap_year):
    days_of_month = [31, 29 if leap_year else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    return sum(days_of_month[:month-1])

while True:
    date = input("Enter date (dd-mm-yy): ")
    patern = r"\d{1,2}-\d{1,2}-\d{1,}"  #   Date Format
    verify = re.match(patern,date)
    
    if verify:
        dates = date.split("-")
        if len(dates) > 3:
            print("\nInvalid date format, please try again.\n")
            continue
        day = int(dates[0])
        month = int(dates[1])      #  Separate day, month and year
        year = int(dates[2])
        leap_year = is_leap_year(year)
        
        if (1 <= day <= 31 and 1 <= month <= 12 and year >= 0):
            if (month == 2 and ((leap_year and day <= 29) or (not leap_year and day <= 28))) or \
               (month in [4, 6, 9, 11] and day <= 30) or \
               (month in [1, 3, 5, 7, 8, 10, 12] and day <= 31): break
        else:
            print("\nInvalid date format, please try again.\n")
            continue
    else:
        print("\nInvalid date format, please try again.\n")
        continue

day_of_year = days_per_month(month, leap_year) + day
total_days = 366 if leap_year else 365
print(f"Date: {date}\nDay of the year: {day_of_year} of {total_days}\nDays remaining: {total_days - day_of_year}")