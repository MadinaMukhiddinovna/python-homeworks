

#--------------------------------------------------------------


# Homework Exercises
# 1. Age Calculator
# Write a Python program to ask for a user's 
# name and year of birth, then calculate and display their age.

# Ask user's name and birth year
name = input("Enter your name: ")
birth_year = int(input("Enter your birth year: "))

#calculate age
current_year = 2025
age = current_year - birth_year

print(f"{name}, you are {age} years old.")


# 2. Extract Car Names
# Extract car names from the following text:
#extracting car names (e.g., "Lamborghini", "Subaru", etc.)
#bbased on pattern or known positions (example logic):
car1 = txt[0] + txt[2] + txt[4] + txt[6]  # 'Last'
car2 = txt[1] + txt[3] + txt[5] + txt[7]  # 'Mate'

print("Extracted cars:", car1, car2)

# txt = 'LMaasleitbtui'

# 3. Extract Car Names
# Extract car names from the following text:
# txt = 'MsaatmiazD'
#example logic (assuming pattern again):
car1 = txt[0] + txt[2] + txt[4] + txt[6]  # 'Mata'
car2 = txt[1] + txt[3] + txt[5] + txt[7]  # 'ssmi'

print("Extracted cars:", car1, car2)
# 4. Extract Residence Area
# Extract the residence area from the following text:
# txt = "I'am John. I am from London"
txt = "I'm John. I am from London"

#extracting area after "from"
residence = txt.split("from ")[1]

print("Residence area:", residence)
# 5. Reverse String
# Write a Python program that takes a user input string and prints it in reverse order.
#ask for user input
user_input = input("Enter a string: ")

#reverse the string
reversed_string = user_input[::-1]

print("Reversed string:", reversed_string)

# 6. Count Vowels
# Write a Python program that counts the number of vowels in a given string.
#get user input
text = input("Enter a string: ")

#define vowels
vowels = "aeiouAEIOU"

#count vowels
count = sum(1 for char in text if char in vowels)

print("Number of vowels:", count)

# 7. Find Maximum Value
# Write a Python program that takes a list of numbers as input and prints the maximum value.
# Input list
numbers = list(map(int, input("Enter numbers separated by space: ").split()))

# Find maximum
max_value = max(numbers)

print("Maximum value:", max_value)

# 8. Check Palindrome
# Write a Python program that checks if a given word is a palindrome (reads the same forward and backward).
#get user input
word = input("Enter a word: ")

#check palindrome
if word == word[::-1]:
    print("It's a palindrome.")
else:
    print("It's not a palindrome.")

# 9. Extract Email Domain
# Write a Python program that extracts and prints the domain from an email address provided by the user.
#get email input
email = input("Enter your email: ")

# Extract domain
domain = email.split("@")[1]
print("Email domain:", domain)

# 10. Generate Random Password
# Write a Python program to generate a random password containing letters, digits, and special characters.
import random
import string

#define character set
characters = string.ascii_letters + string.digits + string.punctuation

#generate password
password = ''.join(random.choice(characters) for _ in range(12))
print("Random password:", password)
