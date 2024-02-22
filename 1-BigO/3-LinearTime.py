# O(n) Linear Time Complexity: The time complexity of an algorithm is said to be linear if the time taken by the algorithm is directly proportional to the size of the input.
# Pros:
# 1. Efficient for large inputs: Linear time algorithms are efficient for large input sizes since the time taken increases linearly with the input size.
# 2. Scalable: Linear time algorithms can handle large inputs without a significant increase in execution time, making them scalable.
# 3. Flexibility: Linear time complexity can be used to solve a wide range of problems and is suitable for a variety of applications.
# 4. Simplifies algorithm analysis: Linear time complexity simplifies the analysis of algorithms and allows for easier comparison between different algorithms.
# Cons:
# 1. Limited performance: Linear time algorithms may not be able to achieve the same level of performance as algorithms with lower time complexity.
# 2. Inefficient for small inputs: Linear time algorithms may be less efficient for small input sizes since the time taken increases with the input size.
# 3. Complexity: Linear time algorithms may be more complex to implement and analyze compared to algorithms with lower time complexity.
# 4. Limited applicability: Linear time algorithms may not be suitable for all problems and may not be efficient for small input sizes.

def find_max(array):
    max_value = array[0]
    for element in array[1:]:
        if element > max_value:
            max_value = element
    return max_value

def find_max2(array):
    return max(array)

def linear_search(arr, target):
    for i, element in enumerate(arr):
        if element == target:
            return i
    return -1  # Element not found

def linear_search2(arr, target):
  try:
    return arr.index(target)
  except ValueError:
    return -1

def fn(n):
    for i in range(n):
        print(i)


def sum_elements(arr):
    total_sum = 0
    for element in arr:
        total_sum += element
    return total_sum


def count_occurrences(arr, target):
    count = 0
    for element in arr:
        if element == target:
            count += 1
    return count
  
def count_occurrences2(arr, target):
  return arr.count(target)

# the for loop has a time complexity of O(n) and the while loop has a time complexity of O(log n)
def print_values(n):
    for i in range(n):
        print(i)
    j = 1
    while j <= n:
        print(j)
        j *= 2

# the first while loop has a time complexity of O(log n) and the second while loop has a time complexity of O(log n)
def print_values2(n):
    i = 1
    while i <= n:
        print(i)
        i *= 2
    j = 1
    while j <= n:
        print(j)
        j *= 2

print("Max of [1, 2, 3, 4, 5, 6]: ", find_max([1, 2, 3, 4, 5, 6]))
print("Max of [1, 2, 3, 4, 5, 6]: ", find_max2([1, 2, 3, 4, 5, 6]))
print("Linear Search of [1, 2, 3, 4, 5, 6] is index: ", linear_search([1, 2, 3, 4, 5, 6], 3))
print("Linear Search of [1, 2, 3, 4, 5, 6] is index: ", linear_search2([1, 2, 3, 4, 5, 6], 3))
print("fn of 5: ", fn(5))
print("Sum of [1, 2, 3, 4, 5, 6]: ", sum_elements([1, 2, 3, 4, 5, 6]))
print("Count of occurrences of 3 in [1, 2, 3, 4, 5, 6]: ", count_occurrences([1, 2, 3, 4, 5, 6], 3))
print("Count of occurrences of 3 in [1, 2, 3, 4, 5, 6]: ", count_occurrences2([1, 2, 3, 4, 5, 6], 3))

print('example1:')
print_values(10)
print('example2:')
print_values2(10)