""" Current timezones at Different places """

from datetime import datetime as dt
import pytz
#pytz ---> python timezones

timezones=pytz.all_timezones

for i in range(len(timezones)):
    zone=timezones[i]
    tz=pytz.timezone(zone)
    print("Current time at zone ",zone,"is ",dt.now(tz))