import re

# Replace all white-space characters with the digit "9":
txt = "The rain in Spain"
x = re.sub("\s", '[0-9]', txt)
print(x)