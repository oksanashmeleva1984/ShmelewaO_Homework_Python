def is_year_leap(year):
    return 'True' if year % 4 == 0 else 'False'


check_year = 2024
result = is_year_leap(check_year)
print(f'год {check_year} : {result}')
