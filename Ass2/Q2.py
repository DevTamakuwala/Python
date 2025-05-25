# Q2Write a function max_element(numbers) that returns the maximum element from a given list of
# numbers.
def max_element(numbers):
    max_num = numbers[0]
    for num in numbers:
        if num > max_num:
            max_num = num
    return max_num

# Example usage:
lst = list(map(int, input("Enter numbers separated by spaces: ").split()))
print("Maximum Element:", max_element(lst))
