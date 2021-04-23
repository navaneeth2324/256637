#Write a Python program to get next day of a given date using if-elif-else
year = int(input("year: "))

if year%400==0:
    leap=True
elif year%4==0:
    leap=True
elif year%100==0:
    leap=False
else:
    leap=False

month = int(input("month:"))

if month in (1, 3, 5, 7, 8, 10, 12):
    days = 31
elif month == 2:
    if leap:
        days = 29
    else:
        days = 28
else:
    days = 30


day = int(input("day:"))

if day < days:
    day += 1
else:
    day = 1
    if month == 12:
        month = 1
        year += 1
    else:
        month += 1
print("The next date %d|%d|%d." % (day,month,year))