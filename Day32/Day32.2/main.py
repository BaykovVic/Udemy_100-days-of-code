import datetime as dt
from calendar import weekday

now = dt.datetime.now()

year = now.year
month = now.month

weekday = now.weekday()
print(weekday, month, year)

dat_of_birth = dt.datetime(year=1900, month=1, day=1)
print(dat_of_birth)