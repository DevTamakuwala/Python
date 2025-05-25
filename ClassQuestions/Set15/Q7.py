text = input("Enter a string: ").lower()
vowels = "aeiou"
vowel_count = consonant_count = 0

for char in text:
    if char.isalpha():
        if char in vowels:
            vowel_count += 1
        else:
            consonant_count += 1

print("Vowels:", vowel_count)
print("Consonants:", consonant_count)

if text == text[::-1]:
    print("Palindrome")
else:
    print("Not a palindrome")
