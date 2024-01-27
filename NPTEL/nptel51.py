""" Finding the day of week of date """
""" year 1444 is not getting with this program """

import calendar

def check_leap(y):
    if y%100==0:
        if y%400==0:
            return True
        else:
            return False
    elif y%4==0:
        return True
    else:
        return False
    
def check_date(dt,m,y,l):
    if l:
        if m==2:
            if dt<30 or dt>0:
                return True
            else: 
                return False
    else:
        if m==2:
            if dt<29 or dt>0:
                return True
            else: 
                return False
        if m<8:
            if m%2==1:
                if dt<32 or dt>0:
                    return True
                else:
                    return False
            else:
                if dt<31 or dt>0:
                    return True
                else:
                    return False
        else:
            if m%2==0:
                if dt<32 or dt>0:
                    return True
                else:
                    return False
            else:
                if dt<31 or dt>0:
                    return True
                else:
                    return False
                
def get_day(i):
    list_of_days=["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
    return list_of_days[i]

while(1):
    year=int(input("Enter the year"))
    if(year<1 or year>100000):
        print("Enter a valid year! (1-12)")
    else:
        break

while(1):
    month=int(input("Enter the month (1-12)"))
    if(month<1):
        print("Enter a valid month! (1-12)")
    elif(month>12):
        print("Enter a valid month! (1-12)")    
    else:
        break

leap=check_leap(year)

while(1):
    date=int(input("Enter the date"))
    if check_date(date,month,year,leap):
        break
    else:
        print("Enter a valid date")
        
day_index=calendar.weekday(year,month,date)
day= get_day(day_index)

print(date,"/",month,"/",year," falls on ",day)