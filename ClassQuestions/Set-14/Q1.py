import re

text = "Today is 10-04-2025 and tomorrow is 11-04-2025."

# 1. finditer()
print("finditer():")
for match in re.finditer(r'\d{2}-\d{2}-\d{4}', text):
    print(match.group())

# 2. match()
print("\nmatch():")
match_result = re.match(r'tomorrow', text)
print(match_result.group() if match_result else "No match")

# 3. fullmatch()
print("\nfullmatch():")
fullmatch_result = re.fullmatch(r'Today is.*2025\.', text)
print(fullmatch_result.group() if fullmatch_result else "No full match")

# 4. search()
print("\nsearch():")
search_result = re.search(r'\d{4}', text)
print(search_result.group() if search_result else "Not found")

# 5. findall()
print("\nfindall():")
print(re.findall(r'\d{2}-\d{2}-\d{4}', text))

# 6. sub()
print("\nsub():")
print(re.sub(r'\d{2}-\d{2}-\d{4}', 'DATE', text))

# 7. split()
print("\nsplit():")
print(re.split(r'\s+', text))
