from datetime import datetime

year = int(input("Enter a year: "))

try:
    datetime(year, 2, 29)
    print(f"{year} is a leap year")
except ValueError:
    print(f"{year} is not a leap year")
