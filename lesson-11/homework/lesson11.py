#hw_11
#math_operations.py
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b

#string_utils.py
def reverse_string(s):
    return s[::-1]

def count_vowels(s):
    vowels = "aeiouAEIOU"
    return sum(1 for char in s if char in vowels)
#geometry/circle.py
import math

def calculate_area(radius):
    return math.pi * radius ** 2

def calculate_circumference(radius):
    return 2 * math.pi * radius
#file_operations/file_reader.py
def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        return f.read()
#file_operations/file_writer.py
def write_file(file_path, content):
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
      
import math_operations as mo
import string_utils as su
from geometry.circle import calculate_area, calculate_circumference
from file_operations.file_reader import read_file
from file_operations.file_writer import write_file

print(mo.add(5, 3))  # 8
print(su.reverse_string("hello"))  # "olleh"
print(calculate_area(5))  # 78.53981633974483
print(calculate_circumference(5))  # 31.41592653589793

write_file("example.txt", "Hello, world!")
content = read_file("example.txt")
print(content)  # Hello, world!
