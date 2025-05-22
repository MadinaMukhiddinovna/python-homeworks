# 1. Create and Access List Elements
# Create a list containing five different fruits and print the third fruit.
fruits = ["apple", "banana", "orange", "grape", "mango"]
print(fruits[2])  # Index starts from 0

# 2. Concatenate Two Lists
# Create two lists of numbers and concatenate them into a single list.
list1 = [1, 2, 3]
list2 = [4, 5, 6]
combined = list1 + list2
print(combined)
#used + to join two lists

# 3. Extract Elements from a List
# Given a list of numbers, extract the first, middle, and last elements and store them in a new list.
numbers = [10, 20, 30, 40, 50]
first = numbers[0]
middle = numbers[len(numbers)//2]
last = numbers[-1]
new_list = [first, middle, last]
print(new_list)
#got first, middle, last using indexing

# 4. Convert List to Tuple
# Create a list of your five favorite movies and convert it into a tuple.
movies = ["Avatar", "Interstellar", "Inception", "Matrix", "Titanic"]
movies_tuple = tuple(movies)
print(movies_tuple)

# 5. Check Element in a List
# Given a list of cities, check if "Paris" is in the list and print the result.
cities = ["London", "Paris", "Rome", "Berlin"]
is_in_list = "Paris" in cities
print(is_in_list)

# 6. Duplicate a List Without Using Loops
# Create a list of numbers and duplicate it without using loops.
numbers = [1, 2, 3]
duplicated = numbers * 2
print(duplicated)

# 7. Swap First and Last Elements of a List
# Given a list of numbers, swap the first and last elements.
nums = [10, 20, 30, 40]
nums[0], nums[-1] = nums[-1], nums[0]
print(nums)

# 8. Slice a Tuple
# Create a tuple of numbers from 1 to 10 and print a slice from index 3 to 7.
numbers = tuple(range(1, 11))
print(numbers[3:8])

# 9. Count Occurrences in a List
# Create a list of colors and count how many times "blue" appears in the list.
colors = ["red", "blue", "green", "blue", "yellow", "blue"]
count = colors.count("blue")
print(count)

# 10. Find the Index of an Element in a Tuple
# Given a tuple of animals, find the index of "lion".
animals = ("cat", "dog", "lion", "tiger")
index = animals.index("lion")
print(index)

# 11. Merge Two Tuples
# Create two tuples of numbers and merge them into a single tuple.
t1 = (1, 2, 3)
t2 = (4, 5, 6)
merged = t1 + t2
print(merged)

# 12. Find the Length of a List and Tuple
# Given a list and a tuple, find and print their lengths.
my_list = [1, 2, 3, 4]
my_tuple = (10, 20, 30)
print(len(my_list))
print(len(my_tuple))

# 13. Convert Tuple to List
# Create a tuple of five numbers and convert it into a list.
nums = (1, 2, 3, 4, 5)
nums_list = list(nums)
print(nums_list)

# 14. Find Maximum and Minimum in a Tuple
# Given a tuple of numbers, find and print the maximum and minimum values.
values = (7, 2, 9, 4, 1)
print("Max:", max(values))
print("Min:", min(values))

# 15. Reverse a Tuple
# Create a tuple of words and print it in reverse order.
words = ("one", "two", "three", "four")
reversed_tuple = words[::-1]
print(reversed_tuple)

