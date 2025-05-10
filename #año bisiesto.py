#año bisiesto
def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
year = 2024
print(f"{year} es bisiesto: {is_leap_year(year)}")