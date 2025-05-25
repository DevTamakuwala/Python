import re

def check_lower_underscore(string):
    pattern = r'^[a-z_]+$'
    return "Valid" if re.fullmatch(pattern, string) else "Invalid"

print(f"hello_world: {check_lower_underscore("hello_world")}")
print(f"Hello_World: {check_lower_underscore("Hello_World")}")
print(f"hello123b: {check_lower_underscore("hello123b")}")
