import calendar

month = int(input("Enter month: "))
year = int(input("Enter Year: "))

print("Number of days in the month: ",calendar.monthrange(year,month)[1])


