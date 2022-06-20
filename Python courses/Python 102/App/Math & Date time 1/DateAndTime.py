import  datetime
#create date => atetime.date(year, month, day)
date =datetime.date(2021, 9, 27)
print(date) #2021-09-27
print(date.year) #2121
print(date.month) #9
print(date.day) #27

#create time => atetime.date(hour, minute, second)
time = datetime.time(14, 33, 15)
print(time) #14:33:15
print(time.hour) #14
print(time.minute) #33
print(time.second) #15

#current day & time
now = datetime.datetime.today()
print(now)
print(now.year)
print(now.month)
print(now.day)
print(now.hour)
print(now.minute)
print(now.second)

#convwert date & time to string
print(date.strftime('%A %B %y')) #Monday September 21
# '%A' full day name
# '%B' full month name
# '%Y' full year numbers
# '%y'  short year numbers

print(time.strftime('%I %M %S')) #02 33 15
# '%I' convert to 12hours system
# '%H' 24 hours sys
# '%P' PM or AM
# %B full month name
# %b short month name
# %m month number
#  '%M' muntits
