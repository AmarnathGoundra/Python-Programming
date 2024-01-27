""" date time """

import datetime
a=datetime.date.today()
b=datetime.date.today().strftime("%Y")
c=datetime.date.today().strftime("%B")
d=datetime.date.today().strftime("%d")
e=datetime.date.today().strftime("%W")
f=datetime.date.today().strftime("%w")
g=datetime.date.today().strftime("%j")
h=datetime.date.today().strftime("%A")
i=datetime.datetime.now()
print("date",a)
print("year",b)
print("month",c)
print("day",d)
print("week of year",e)
print("week of month",f)
print("day of the year",g)
print("day of week",h)
print("present date & time",i)

day=int(1)
month=int(2)
year=2022
dd=datetime.date(year,month,day)
print(dd)
day=dd.timetuple().tm_yday
print(day)