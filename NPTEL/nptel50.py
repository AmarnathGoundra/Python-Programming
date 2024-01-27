""" working with datetime, calender and time zone """

from datetime import datetime as dt

#present time
print(dt.now())

import pytz
#tz = time zone

tz=pytz.timezone('Singapore')
#for India: 'Asia/Kolkata'

#present time at that zone
print(dt.now(tz))

# printing all timezones
#print(pytz.all_timezones)

#number of time zones
print(len(pytz.all_timezones))

# Calender
import calendar

#knowing format of weekday using following command in console
# calendar.weekday?

print(calendar.weekday(1444,3,13))

print(calendar.weekday(2022,4,9))