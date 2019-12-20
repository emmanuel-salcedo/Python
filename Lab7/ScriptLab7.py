# 2.	Import datetime and time modules
import datetime

# 3.	Print today’s date
today = datetime.datetime.now()
print("Today’s Date", today)

# 4.	Subtract 3 weeks / 2 days  / 3 hours from todays date
threeweeks = datetime.timedelta(weeks=3)
twodays = datetime.timedelta(days=2)
threehours = datetime.timedelta(hours=3)
newdate = today - threehours - threeweeks - twodays
print("3 Weeks/2 Days/3 Hours Ago: ", newdate)

# 5.	Extract each from today’s date
#       a.	Year
print("Year: ", today.year)
#       b.	Month
print("Month: ", today.month)
#       c.	Day
print("Day: ", today.day)
#       d.	Hour
print("Hour: ", today.hour)
#       e.	Minute
print("Minute: ", today.minute)
#       f.	Seconds
print("Second: ", today.second)
# 6.	Then format the date (YY,MM,DD HH,MM,SS)
print(today.strftime("%y,%m,%d %I,%M,S"))
