def is_prime(number):
    if number < 2:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True

def max_element(numbers):
    max_num = numbers[0]
    for num in numbers:
        if num > max_num:
            max_num = num
    return max_num

def count_vowels(s):
    count = 0
    vowels = "aeiouAEIOU"
    for char in s:
        if char in vowels:
            count += 1
    return count

def remove_duplicates(lst):
    unique_list = []
    for item in lst:
        if item not in unique_list:
            unique_list.append(item)
    return unique_list

def sum_even(lst):
    total = 0
    for num in lst:
        if num % 2 == 0:
            total += num
    return total

while True:
    print("\nMenu:")
    print("A. Check for Prime Number")
    print("B. Find Maximum Element in a List")
    print("C. Count Vowels in a String")
    print("D. Remove Duplicates from a List")
    print("E. Sum of Even Numbers in a List")
    print("F. Exit")

    choice = input("Enter your choice (A-F): ").strip().upper()

    if choice == "A":
        num = int(input("Enter a number: "))
        print("Prime:", is_prime(num))
    elif choice == "B":
        lst = list(map(int, input("Enter numbers separated by spaces: ").split()))
        print("Maximum Element:", max_element(lst))
    elif choice == "C":
        text = input("Enter a string: ")
        print("Vowel Count:", count_vowels(text))
    elif choice == "D":
        lst = list(map(int, input("Enter numbers separated by spaces: ").split()))
        print("List after removing duplicates:", remove_duplicates(lst))
    elif choice == "E":
        lst = list(map(int, input("Enter numbers separated by spaces: ").split()))
        print("Sum of Even Numbers:", sum_even(lst))
    elif choice == "F":
        print("Exiting program.")
        break
    else:
        print("Invalid choice. Please try again.")
