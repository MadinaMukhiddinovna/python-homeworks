
#lesson.5

def is_leap(year):
    """
    Determines whether a given year is a leap year.
    
    A year is a leap year if:
    - It is divisible by 4, and
    - It is NOT divisible by 100, unless it is also divisible by 400.
    
    Parameters:
    year (int): The year to be checked.
    
    Returns:
    bool: True if the year is a leap year, False otherwise.
    """
    if not isinstance(year, int):
        raise ValueError("Year must be an integer.")
    
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

# Example:
print(is_leap(2020))  # True
print(is_leap(1900))  # False
print(is_leap(2000))  # True

n = int(input("Enter an integer (1 to 100): "))

if n % 2 != 0:
    print("Weird")
elif 2 <= n <= 5:
    print("Not Weird")
elif 6 <= n <= 20:
    print("Weird")
else:
    print("Not Weird")


a = int(input("Enter first integer a: "))
b = int(input("Enter second integer b: "))

def evens_if_else(a, b):
    if a > b:
        a, b = b, a  # swap to ensure a <= b
    
    evens = []
    current = a
    while current <= b:
        if current % 2 == 0:
            evens.append(current)
        current += 1
    return evens

print("Even numbers between a and b (inclusive) with if-else:", evens_if_else(a, b))


a = int(input("Enter first integer a: "))
b = int(input("Enter second integer b: "))

def evens_no_if_else(a, b):
    # Swap if a > b without if-else using min/max
    start, end = min(a, b), max(a, b)
    return list(filter(lambda x: x % 2 == 0, range(start, end + 1)))

print("Even numbers between a and b (inclusive) without if-else:", evens_no_if_else(a, b))


#======================================================================================================================
