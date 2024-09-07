# How to get the current day and date, using the DateTime module

import datetime as dt

now = dt.datetime.now()
print(now)
print(type(now))

# With this method we can change the way the date and time appear as we wish.
# Very important if they are uppercase or lowercase they can screw everything up
print(now.strftime('%d/%m/%Y %H:%M:%S'))
print(now.strftime('%d/%m/%y %H:%M:%S')) # Simplify the 4-digit year to just 2