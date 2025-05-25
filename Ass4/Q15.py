# 1. Python Program to Read the First n Lines of a File
def read_first_n_lines(file_name, n):
    with open(file_name, 'r') as file:
        lines = file.readlines()
        print(f"First {n} lines of the file:")
        for i in range(min(n, len(lines))):
            print(lines[i].strip())


# 2. Python Program to Append Text to a File and Display the Text
def append_text_to_file(file_name, text):
    with open(file_name, 'a') as file:
        file.write(text + '\n')

    # Displaying the content of the file
    print("\nContent of the file after appending text:")
    with open(file_name, 'r') as file:
        print(file.read())


# 3. Python Program to Read the Last n Lines of a File
def read_last_n_lines(file_name, n):
    with open(file_name, 'r') as file:
        lines = file.readlines()
        print(f"\nLast {n} lines of the file:")
        for line in lines[-n:]:
            print(line.strip())


# 4. Python Program to Read a File Line by Line and Store it Into a List
def read_lines_into_list(file_name):
    with open(file_name, 'r') as file:
        lines = file.readlines()
        print("\nReading file line by line and storing into list:")
        lines_list = [line.strip() for line in lines]
        print(lines_list)


# Example usage
file_name = 'example.txt'  # Make sure to create this file with some content

# Read first 3 lines
read_first_n_lines(file_name, 3)

# Append text to file and display content
text_to_append = "This is a new line added to the file."
append_text_to_file(file_name, text_to_append)

# Read last 2 lines
read_last_n_lines(file_name, 2)

# Read file line by line and store in a list
read_lines_into_list(file_name)
