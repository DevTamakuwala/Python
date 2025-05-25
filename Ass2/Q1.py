# Q1-Write a function is_prime(number) that checks if a number is prime. The function should return
# True if the number is prime, otherwise False.

def is_prime(number):
    if number < 2:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True

# Example usage:
num = int(input("Enter a number: "))
print("Prime:", is_prime(num))
