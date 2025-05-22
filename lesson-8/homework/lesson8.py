
#lesson-8
#1 Handle ZeroDivisionError
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")

#2 Raise ValueError if input is not an integer
try:
    user_input = input("Enter an integer: ")
    num = int(user_input)
    print(f"You entered: {num}")
except ValueError:
    print("Error: Invalid integer input.")
#3. Handle FileNotFoundError when opening a file
try:
    with open("nonexistent_file.txt", "r") as file:
        content = file.read()
except FileNotFoundError:
    print("Error: File not found.")
#4. Raise TypeError if inputs are not numbers
try:
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    print(f"Sum: {a + b}")
except ValueError:
    print("Error: Input must be a number.")
#5. Handle PermissionError when opening a file
try:
    with open("/root/secret.txt", "r") as file:
        data = file.read()
except PermissionError:
    print("Error: Permission denied while accessing the file.")
#6. Handle IndexError in list operation
my_list = [1, 2, 3]
try:
    print(my_list[5])
except IndexError:
    print("Error: List index out of range.")
#7. Handle KeyboardInterrupt during user input
try:
    num = input("Enter a number: ")
except KeyboardInterrupt:
    print("\nInput cancelled by user.")
#8. Handle ArithmeticError during division
try:
    a = 10
    b = 0
    result = a / b
except ArithmeticError:
    print("Error: Arithmetic error occurred during division.")
#9. Handle UnicodeDecodeError when reading a file
try:
    with open("file.txt", "r", encoding="utf-8") as f:
        content = f.read()
except UnicodeDecodeError:
    print("Error: File encoding issue detected.")
#10. Handle AttributeError on list operation
my_list = [1, 2, 3]
try:
    my_list.push(4)  # 'push' is not a valid list method
except AttributeError:
    print("Error: Attribute does not exist.")
#11. Read entire text file
with open("example.txt", "r") as file:
    content = file.read()
    print(content)
#12. Read first n lines of a file
n = 3
with open("example.txt", "r") as file:
    for i in range(n):
        line = file.readline()
        if not line:
            break
        print(line.strip())

#13. Append text to a file and display content
with open("example.txt", "a") as file:
    file.write("Appended line.\n")

with open("example.txt", "r") as file:
    print(file.read())

#14. Read last n lines of a file
n = 3
with open("example.txt", "r") as file:
    lines = file.readlines()
    for line in lines[-n:]:
        print(line.strip())
#15. Read file line by line into a list
with open("example.txt", "r") as file:
    lines = file.readlines()
print(lines)
#16. Read file line by line into a variable (string)
with open("example.txt", "r") as file:
    content = file.read()
print(content)
#17. Read file line by line into an array (list)
lines = []
with open("example.txt", "r") as file:
    for line in file:
        lines.append(line.strip())
print(lines)
#18. Find longest words in a file
with open("example.txt", "r") as file:
    words = file.read().split()
    longest_length = max(len(word) for word in words)
    longest_words = [word for word in words if len(word) == longest_length]
print("Longest words:", longest_words)
#19. Count the number of lines in a text file
with open("example.txt", "r") as file:
    line_count = sum(1 for line in file)
print(f"Number of lines: {line_count}")
#20. Count the frequency of words in a file
from collections import Counter

with open("example.txt", "r") as file:
    text = file.read().lower()
    words = text.split()
    frequency = Counter(words)
print(frequency)
#from collections import Counter

with open("example.txt", "r") as file:
    text = file.read().lower()
    words = text.split()
    frequency = Counter(words)
print(frequency)
#21. Get the file size of a plain file
import os

file_size = os.path.getsize("example.txt")
print(f"File size: {file_size} bytes")
#22. Write a list to a file
lines_to_write = ["Line 1", "Line 2", "Line 3"]
with open("output.txt", "w") as file:
    for line in lines_to_write:
        file.write(line + "\n")
#23. Copy the contents of a file to another file
with open("example.txt", "r") as source_file:
    content = source_file.read()

with open("copy.txt", "w") as dest_file:
    dest_file.write(content)
#24. Combine each line from the first file with the corresponding line in the second file
with open("file1.txt", "r") as f1, open("file2.txt", "r") as f2:
    for line1, line2 in zip(f1, f2):
        combined = line1.strip() + " " + line2.strip()
        print(combined)
#25. Read a random line from a file
import random

with open("example.txt", "r") as file:
    lines = file.readlines()
random_line = random.choice(lines).strip()
print(random_line)
#26. Check if a file is closed or not
file = open("example.txt", "r")
print(f"File closed? {file.closed}")
file.close()
print(f"File closed? {file.closed}")
#27. Remove newline characters from a file
with open("example.txt", "r") as file:
    lines = [line.strip() for line in file]
print(lines)
#28. Count the number of words in a given text file (words may be comma-separated without space)
import re

with open("example.txt", "r") as file:
    text = file.read()
# Split by spaces or commas without spaces
words = re.split(r'[,\s]+', text.strip())
word_count = len([w for w in words if w])
print(f"Number of words: {word_count}")
#29. Extract characters from various text files and put them into a list
with open("example.txt", "r") as file:
    content = file.read()
chars = list(content)
print(chars)
#30. Generate 26 text files named A.txt, B.txt, ..., Z.txt
import string

for letter in string.ascii_uppercase:
    filename = f"{letter}.txt"
    with open(filename, "w") as f:
        f.write(f"This is file {filename}\n")
#31. Create a file with all English letters listed with specified number of letters on each line
import string

letters = string.ascii_lowercase
n = 5  # letters per line

with open("alphabet.txt", "w") as file:
    for i in range(0, len(letters), n):
        line = letters[i:i+n]
        file.write(line + "\n")


