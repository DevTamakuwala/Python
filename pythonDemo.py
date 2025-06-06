"""
List = [] = mutable
Tuple = () = immutable
Dictionary = {"key": value, "key": value} = mutable
Range = range(10)
Set = {} = mutable
String = "" = immutable

List operations
.append() = add an element at the end
.insert() = add an element at a specific position
.remove() = remove an element
.pop() = remove an element at specific position
.clear() = remove all elements
.sort() = sort elements
.reverse() = reverse elements
.copy() = copy elements

[1:3] = slicing
elements from 1 up to 3 (3rd index NOT included)

[1: ]
elements from 1 to end

[: 3]
elements from start to 3 (3rd index NOT included)

[:: -1]
reverse element

[1::-1]
reverse elements from 0 to 1
"""
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

print()
fruits = ['apple', 'cherry', 'banana']
fruits += ['kiwi']

print(fruits)
print(fruits[1::-1])
fruits.sort()
print(fruits)

for fruit in fruits:
    print(fruit)


fruits = {"apple", "banana", "cherry", "apple"}
print(fruits)
fruits.add("kiwi")
print(fruits)
fruits.discard("banana")
print(fruits)
print(type(fruits))