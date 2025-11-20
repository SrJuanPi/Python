import datetime

birthday = input("Enter your birthday (dd/mm): ")
birthdayDay = int(datetime.datetime.strftime(birthday, "%d"))
birthdayMonth = int(datetime.datetime.strftime(birthday, "%m"))

actualDate = datetime.datetime.now()
actualDay = int(datetime.datetime.strftime(actualDate, '%d'))
actualMonth = int(datetime.datetime.strftime(actualDate, '%m'))
actualYear = int(datetime.datetime.strftime(actualDate, "%Y"))


def time_to_birthday(birthdayDay, birthdayMonth, actualDay, actualMonth):
    if actualMonth < birthdayMonth:
        months_remaining = birthdayMonth - actualMonth
        days_remaining = birthdayDay
        
    elif actualMonth == birthdayMonth and actualDay < birthdayDay:
        days_remaining = birthdayDay
        
    elif actualMonth > birthdayMonth:
        months_remaining = birthdayMonth + (12-actualMonth)
        days_remaining = birthdayDay + ()
        
    elif actualMonth == birthdayMonth and actualDay > birthdayDay:...

if birthdayDay == actualDay and birthdayMonth == actualMonth:
    print("Happy BirthDay!")
else: ...

# Need to learn more about the library to simplify the code