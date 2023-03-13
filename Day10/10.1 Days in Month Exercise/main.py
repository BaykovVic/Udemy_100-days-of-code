def is_leap(year):
    result = False
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                result = True
        else:
            result = True
    return result


def days_in_month(year, month):
    if month > 12 and month < 1:
        print("Invalid input")
        return
    month = month - 1
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if month == 1 and is_leap(year):
        return month_days[month] + 1
    return month_days[month]


# 🚨 Do NOT change any of the code below
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)












