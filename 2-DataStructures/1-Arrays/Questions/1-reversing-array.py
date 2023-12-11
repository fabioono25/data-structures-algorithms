# Reversing a list in O(N) + the algorithm must be in-place (no use of additional memory)
# Example: [1, 2, 3, 4, 5] -> [5, 4, 3, 2, 1]

# swap array elements. Time complexity: O(N), Space complexity: O(1)
def reverse_array(arr):
  for i in range(len(arr) // 2):
    arr[i], arr[len(arr) - i - 1] = arr[len(arr) - i - 1], arr[i]
  return arr

# Solution 1: Using a temporary variable. Time complexity: O(N), Space complexity: O(1)
def reverse_array2(arr):
  for i in range(len(arr) // 2):
    temp = arr[i]
    arr[i] = arr[len(arr) - i - 1]
    arr[len(arr) - i - 1] = temp
  return arr

# Solution 2: Using a stack. Time complexity: O(N), Space complexity: O(N)
def reverse_array3(arr):
  stack = []
  for i in range(len(arr)):
    stack.append(arr.pop())
  return stack

# Solution 3: Using recursion. Time complexity: O(N), Space complexity: O(N)
def reverse_array4(arr):
  if len(arr) == 0:
    return []
  return [arr[-1]] + reverse_array4(arr[:-1])

# Solution 4: Using a loop. Time complexity: O(N), Space complexity: O(N)
def reverse_array5(arr):
  reversed_arr = []
  for i in range(len(arr) - 1, -1, -1):
    reversed_arr.append(arr[i])
  return reversed_arr

# Solution 5: Using the built-in reverse() method. Time complexity: O(N), Space complexity: O(1)
def reverse_array6(arr):
  arr.reverse()
  return arr

# Test cases
print(reverse_array([1, 2, 3, 4, 5]))  # [5, 4, 3, 2, 1]
print(reverse_array2([1, 2, 3, 4, 5])) # [5, 4, 3, 2, 1]
print(reverse_array3([1, 2, 3, 4, 5])) # [5, 4, 3, 2, 1]
print(reverse_array4([1, 2, 3, 4, 5])) # [5, 4, 3, 2, 1]
print(reverse_array5([1, 2, 3, 4, 5])) # [5, 4, 3, 2, 1]
print(reverse_array6([1, 2, 3, 4, 5])) # [5, 4, 3, 2, 1]