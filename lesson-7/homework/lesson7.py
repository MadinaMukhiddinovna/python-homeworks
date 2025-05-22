def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Examples
print(is_prime(4))  # False
print(is_prime(7))  # True

#aprime number is only divisible by 1 and itself. We check divisibility up to n

def digit_sum(k):
    return sum(int(digit) for digit in str(k))

# Examples
print(digit_sum(24))   # 6
print(digit_sum(502))  # 7
#convert number to string, iterate over digits, convert to integers, then sum them

 #task 3: Powers of 2 less than or equal to N
def powers_of_two(n):
    i = 1
    while (2 ** i) <= n:
        print(2 ** i, end=' ')
        i += 1

# Example
powers_of_two(10)  # Output: 2 4 8


primes = list(filter(lambda x: is_prime(x), range(1, 51)))
print(primes)
#use filter() with a lambda to keep only prime numbers in range 1–50

sums = list(map(lambda x: digit_sum(x), range(10, 16)))
print(sums)
#use map() to apply digit_sum to every number in the range.
