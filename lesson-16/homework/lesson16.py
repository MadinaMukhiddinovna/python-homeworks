import numpy as np

# 1. Convert List to 1D Array
print("1. Convert List to 1D Array")
original_list = [12.23, 13.32, 100, 36.32]
array_1d = np.array(original_list)
print("Original List:", original_list)
print("One-dimensional NumPy array:", array_1d)
print()

# 2. Create 3x3 Matrix (2–10)
print("2. Create 3x3 Matrix with values from 2 to 10")
matrix = np.arange(2, 11).reshape(3, 3)
print(matrix)
print()

# 3. Null Vector (10) & Update Sixth Value
print("3. Null Vector of size 10 and update 6th value to 11")
null_vector = np.zeros(10)
print("Original null vector:", null_vector)
null_vector[6] = 11
print("Updated vector:", null_vector)
print()

# 4. Array from 12 to 38
print("4. Create array with values from 12 to 38")
array_range = np.arange(12, 38)
print(array_range)
print()

# 5. Convert Array to Float Type
print("5. Convert array to float type")
int_array = np.array([1, 2, 3, 4])
float_array = int_array.astype(float)
print("Original array:", int_array)
print("Converted to float:", float_array)
print()

# 6. Celsius to Fahrenheit Conversion
print("6. Celsius to Fahrenheit Conversion")
celsius = np.array([-17.78, -11.11, 7.34, 1.11, 37.73, 0.])
fahrenheit = celsius * 9 / 5 + 32
print("Values in Centigrade degrees:", celsius)
print("Values in Fahrenheit degrees:", fahrenheit)
print()

# 7. Append Values to Array
print("7. Append values to array")
original_array = np.array([10, 20, 30])
new_values = [40, 50, 60, 70, 80, 90]
appended_array = np.append(original_array, new_values)
print("Original array:", original_array)
print("After append:", appended_array)
print()

# 8. Array Statistical Functions
print("8. Statistical operations on random array")
random_array = np.random.rand(10)
mean = np.mean(random_array)
median = np.median(random_array)
std_dev = np.std(random_array)
print("Random array:", random_array)
print("Mean:", mean)
print("Median:", median)
print("Standard Deviation:", std_dev)
print()

# 9. Find min and max in 10x10 array
print("9. 10x10 array with min and max values")
array_10x10 = np.random.rand(10, 10)
min_val = np.min(array_10x10)
max_val = np.max(array_10x10)
print("Array:\n", array_10x10)
print("Minimum value:", min_val)
print("Maximum value:", max_val)
print()

# 10. Create a 3x3x3 array with random values
print("10. 3x3x3 array with random values")
array_3d = np.random.rand(3, 3, 3)
print(array_3d)

# Task 1: Convert list to array using np.array()
# Task 2: Create a matrix using np.arange() and reshape()
# Task 3: Create zeros with np.zeros() and update index
# Task 4: np.arange() for range of numbers
# Task 5: Use .astype(float) to convert
# Task 6: Apply Celsius to Fahrenheit formula
# Task 7: Use np.append() to add values to the end
# Task 8: Use mean, median, std from NumPy
# Task 9: Use np.min(), np.max() on 2D array
# Task 10: Create 3D array with np.random.rand()
