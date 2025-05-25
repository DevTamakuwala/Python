import re
#QA
def validate_date(date):
    pattern = r'^(0[1-9]|[12][0-9]|3[01])[-/](0[1-9]|1[0-2])[-/](\d{4})$'
    return "Valid Date" if re.fullmatch(pattern, date) else "Invalid Date"

print(validate_date("12-05-2023"))
print(validate_date("32-13-2022"))
print(validate_date("01/01-1999"))

#QB
def validate_float(number):
    pattern = r'^-?\d+\.\d+$'
    return "Valid Float" if re.fullmatch(pattern, number) else "Invalid Float"

print(validate_float("3.14"))
print(validate_float("-0.99"))
print(validate_float(".100"))
print(validate_float("3,14"))
