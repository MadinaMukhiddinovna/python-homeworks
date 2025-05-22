# Lesson 6 - Homework Solutions

# 1. Modify String with Underscores
def modify_string(txt):
    vowels = 'aeiou'
    result = ''
    i = 0
    while i < len(txt):
        result += txt[i]
        if (i + 1) % 3 == 0:
            if txt[i] in vowels or (i + 1 < len(txt) and txt[i + 1] == '_'):
                if i + 1 < len(txt):
                    result += txt[i + 1] + '_'
                    i += 1
            elif i + 1 < len(txt):
                result += '_'
        i += 1
    return result

print(modify_string("hello"))        # hel_lo
print(modify_string("assalom"))      # ass_alom
print(modify_string("abcabcabcdeabcdefabcdefg"))  # abc_abc_abcd_abcd_abcdef

# 2. Integer Squares Exercise
def print_squares(n):
    for i in range(n):
        print(i ** 2)

# Example:
# print_squares(5)

# 3. Loop-Based Exercises
# Exercise 1: Print first 10 natural numbers using while loop
i = 1
while i <= 10:
    print(i)
    i += 1

# Exercise 2: Print the pattern
for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end=' ')
    print()

# Exercise 3: Calculate sum of all numbers from 1 to n
def sum_numbers(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    print(f"Sum is: {total}")

# Exercise 4: Multiplication table of a given number

def multiplication_table(n):
    for i in range(1, 11):
        print(n * i)

# Exercise 5: Display numbers from list using loop
numbers = [12, 75, 150, 180, 145, 525, 50]
for num in numbers:
    if 100 > num > 70:
        print(num)

# Exercise 6: Count digits in number
def count_digits(n):
    print(len(str(n)))

# Exercise 7: Reverse number pattern
for i in range(5, 0, -1):
    for j in range(i, 0, -1):
        print(j, end=' ')
    print()

# Exercise 8: Print list in reverse order
list1 = [10, 20, 30, 40, 50]
for item in reversed(list1):
    print(item)

# Exercise 9: Display numbers -10 to -1
for i in range(-10, 0):
    print(i)

# Exercise 10: Print Done after loop
for i in range(5):
    print(i)
else:
    print("Done!")

# Exercise 11: Prime numbers in range
def print_primes(start, end):
    for num in range(start, end + 1):
        if num > 1:
            for i in range(2, int(num ** 0.5) + 1):
                if num % i == 0:
                    break
            else:
                print(num)

# Exercise 12: Fibonacci series up to 10 terms
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, end=' ')
        a, b = b, a + b
    print()

# Exercise 13: Factorial of number
def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    print(result)

# 4. Return Uncommon Elements of Lists
def uncommon_elements(list1, list2):
    from collections import Counter
    c1, c2 = Counter(list1), Counter(list2)
    result = []
    for key in c1:
        if key not in c2:
            result.extend([key] * c1[key])
        else:
            count_diff = c1[key] - c2[key]
            if count_diff > 0:
                result.extend([key] * count_diff)
    for key in c2:
        if key not in c1:
            result.extend([key] * c2[key])
        else:
            count_diff = c2[key] - c1[key]
            if count_diff > 0:
                result.extend([key] * count_diff)
    return result
print(uncommon_elements([1, 1, 2], [2, 3, 4]))             # [1, 1, 3, 4]
print(uncommon_elements([1, 2, 3], [4, 5, 6]))             # [1, 2, 3, 4, 5, 6]
print(uncommon_elements([1, 1, 2, 3, 4, 2], [1, 3, 4, 5])) # [2, 2, 5]

