# 3. Write a function count_vowels(s) that takes a string and returns the number of vowels (a, e, i, o,
# u) in the string.


def count_vowels(s):
    count = 0
    vowels = "aeiouAEIOU"
    for char in s:
        if char in vowels:
            count += 1
    return count

text = input("Enter a string: ")
print("Vowel Count:", count_vowels(text))
