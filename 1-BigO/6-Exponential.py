# O(2^n) - Exponential Time Complexity: Exponential time complexity is the worst case time complexity. It occurs when the number of operations required to solve a problem doubles with each addition to the input data. It is represented as O(2^n).
# Pros:
# - It is easy to implement.
# - It is a brute-force algorithm.
# Cons:
# - It is not efficient for large inputs.
# - It is not suitable for real-world applications.
# - It is not suitable for real-time applications.

# Example 1
def example1(n):
    if n <= 1:
        return
    example1(n - 1)
    example1(n - 1)

# Example 2: Receiving an array
def example2(arr):
    if not arr:
        return
    arr.pop(0)
    example2(arr)
    example2(arr)

# Subset generation
def subset(arr):
    if not arr:
        return [[]]
    arr.pop(0)
    subsets = subset(arr)
    new_subsets = [([first] + subset) for subset in subsets]
    return subsets + new_subsets

# Fibonacci
def fib(n):
    if n <= 2:
        return 1
    return fib(n - 1) + fib(n - 2)

print("example1(3): ", example1(3))
print("example2([1, 2, 3]): ", example2([1, 2, 3]))
print("subset([1, 2, 3]): ", subset([1, 2, 3]))
print("fib(6): ", fib(6))
