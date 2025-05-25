# 5. Write a function sum_even(lst) that takes a list of numbers and returns the sum of all even
# numbers in the list.

def sum_even(lst):
    total = 0
    for num in lst:
        if num % 2 == 0:  # Check if the number is even
            total += num   # Add even number to total
    return total

# Example usage:
lst = list(map(int, input("Enter numbers separated by spaces: ").split()))
print("Sum of Even Numbers:", sum_even(lst))
