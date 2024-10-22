def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


def days_in_month(leap, month):
    month_days = [31,28,31,30,31,30,31,31,30,31,30,31]
    
    for i in month_days:
        if month > 12 or month < 1:
            return "Invalid input"
        if leap:
            if month == 2:
                return 29
            else:
                return month_days[month-1]
        else:
            return month_days[month-1]



year = int(input("enter the year: "))
month = int(input("enter the month: "))
leap = is_leap(year = year)
days = days_in_month(leap, month)
print(days)