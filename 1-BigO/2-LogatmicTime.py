# O(log n) Logarithmic Time Complexity: The time complexity of an algorithm is said to be logarithmic if the time taken by the algorithm is proportional to the logarithm of the input size.
# Pros:
# 1. Efficient for large inputs: Logarithmic time algorithms are efficient for large input sizes since the time taken increases logarithmically with the input size.
# 2. Scalable: Logarithmic time algorithms can handle large inputs without a significant increase in execution time, making them scalable.
# 3. Flexibility: Logarithmic time complexity can be used to solve a wide range of problems and is suitable for a variety of applications.
# 4. Simplifies algorithm analysis: Logarithmic time complexity simplifies the analysis of algorithms and allows for easier comparison between different algorithms.
# Cons:
# 1. Limited performance: Logarithmic time algorithms may not be able to achieve the same level of performance as algorithms with lower time complexity.
# 2. Inefficient for small inputs: Logarithmic time algorithms may be less efficient for small input sizes since the time taken increases with the input size.
# 3. Complexity: Logarithmic time algorithms may be more complex to implement and analyze compared to algorithms with lower time complexity.
# 4. Limited applicability: Logarithmic time algorithms may not be suitable for all problems and may not be efficient for small input sizes.

# Example 1: Binary search
def binary_search(sorted_array, target):
    left, right = 0, len(sorted_array) - 1

    while left <= right:
        mid = (left + right) // 2
        if sorted_array[mid] == target:
            return mid  # Element found at index mid
        elif sorted_array[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1  # Element not found in the array

# Example 2: Another implementation of binary search
def binary_search_2(array, target):
    start_index, end_index = 0, len(array) - 1
    while start_index <= end_index:
        middle_index = (start_index + end_index) // 2
        if target == array[middle_index]:
            return "Target was found at index " + str(middle_index)
        if target > array[middle_index]:
            print("Searching the right side of Array")
            start_index = middle_index + 1
        if target < array[middle_index]:
            print("Searching the left side of array")
            end_index = middle_index - 1
        else:
            print("Not Found this loop iteration. Looping another iteration.")

    return "Target value not found in array"

# Example 3: Binary search, with recursion
def binary_search_recursive(array, target, start, end):
    if start > end:
        return -1  # Base case: target not found
    mid = (start + end) // 2
    if array[mid] == target:
        return mid  # Base case: target found
    elif array[mid] < target:
        return binary_search_recursive(array, target, mid + 1, end)
    else:
        return binary_search_recursive(array, target, start, mid - 1)

# Example 3: Largest power of two
def largest_power_of_two(n):
    power = 1
    while power * 2 <= n:
        power *= 2
    return power

# Example 4: Count digits
def count_digits(number):
    if number == 0:
        return 1  # 0 has 1 digit
    # Logarithm base 10 gives the number of digits in the integer
    return int(len(str(number)))

print(binary_search([1, 2, 3, 4, 5, 6], 5))
print(binary_search_2([1, 2, 3, 4, 5, 6], 5))
print(binary_search_recursive([1, 2, 3, 4, 5, 6], 5, 0, 5))
print(largest_power_of_two(5))
print(count_digits(1234))
