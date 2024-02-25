# O(n^2) - Quadratic Time: Quadratic time complexity is the worst case time complexity. It occurs when the number of operations required to solve a problem grows quadratically with the size of the input data. It is represented as O(n^2).
# Pros:
# - It is easy to implement.
# - It is suitable for small inputs.
# Cons:
# - It is not efficient for large inputs.
# - It is not suitable for real-world applications.
# - It is not suitable for real-time applications.

# Example 1: Nested for loops
def print_all_pairs(array):
    for i in array:
        for j in array:
            print(i, j)

# Example 2: Bubble sort
def bubble_sort(array):
    for _ in range(len(array)):
        for j in range(len(array)-1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array

# Example 3: String matching
def string_match(str1, str2):
    matches = ""
    for char1 in str1:
        for char2 in str2:
            if char1 == char2:
                matches += char1
    return matches

# Example 4: Nested for loops
def print_all_pairs2(array):
    for i in array:
        for j in array:
            for k in array:
                print(i, j, k)

# Example 5: Another example of O(n^2)
def print_all_pairs3(array):
    for i in array:
        for j in array:
            print(i, j)
    for k in array:
        print(k)

print("Print All Pairs: ")
print_all_pairs([1, 2, 3, 4, 5, 6])

print("Bubble Sort: ", bubble_sort([1, 2, 3, 4, 5, 6]))

print("String Match: ", string_match("hello", "world"))

print("Print All Pairs 2: ")
print_all_pairs2([1, 2, 3, 4, 5, 6])

print("Print All Pairs 3: ")
print_all_pairs3([1, 2, 3, 4, 5, 6])
