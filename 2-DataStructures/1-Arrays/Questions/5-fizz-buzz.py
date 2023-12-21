# FizzBuzz: Given an array of integers, replace all the multiples of 3 by "Fizz", multiples of 5 by "Buzz" and multiples of both 3 and 5 by "FizzBuzz".
# Example: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16] -> 
# [1, 2, "Fizz", 4, "Buzz", "Fizz", 7, 8, "Fizz", "Buzz", 11, "Fizz", 13, 14, "FizzBuzz", 16]

from collections import deque

# Solution 1: Using a loop. Time complexity: O(N), Space complexity: O(1)
def fizz_buzz(arr):
  for i in range(len(arr)):
    if arr[i] % 3 == 0 and arr[i] % 5 == 0:
      arr[i] = "FizzBuzz"
    elif arr[i] % 3 == 0:
      arr[i] = "Fizz"
    elif arr[i] % 5 == 0:
      arr[i] = "Buzz"
  return arr

# Solution 2: Using a queue. Time complexity: O(N), Space complexity: O(N)
def fizz_buzz2(arr):
  queue = deque()
  for i in range(len(arr)):
    if arr[i] % 3 == 0 and arr[i] % 5 == 0:
      queue.append("FizzBuzz")
    elif arr[i] % 3 == 0:
      queue.append("Fizz")
    elif arr[i] % 5 == 0:
      queue.append("Buzz")
    else:
      queue.append(arr[i])

  # convert queue to list, before returning
  return list(queue)

# testing
print(fizz_buzz([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]))
print(fizz_buzz2([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]))