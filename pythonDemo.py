list1 = [1, 2, 3, 4]

print(list1)
print(type(list1))

tuple1 = (1, 2, 3, 4)

print(tuple1)
print(type(tuple1))

dict1 = {"Name": "Dev", "Marks": 10}

print(dict1)
print(type(dict1))

range1 = range(10)

print(range1)
print(type(range1))

set1 = {1, 2, 3, 4, 5}

print(set1)
print(type(set1))

str1 = "Hello It's Dev"

print(str1)
print(type(str1))


a = 10
b = 0
result=None

try:
    result = a / b
except ZeroDivisionError:
    print(ZeroDivisionError)
finally:
    print("Finally block")


match result:
    case None:
        print("There is some problem")

    case _:
        print(result)

for i in range(1, 11):
    print(i, end=" ")
print()
i = 0

while i < 10:
    i += 1
    print(i, end=" ")

