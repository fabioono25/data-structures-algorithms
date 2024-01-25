# giving an array of integers and a number k, find the maximum sum of a subarray of size k.
# example: [1, 2, 3, 4, 5, 6, 7, 8, 9], k = 3 -> 24
# example: [1, 2, 3, 4, 5, 6, 7, 8, 9], k = 4 -> 30

# Brutal force solution
# Time complexity: O(n*k)
# Space complexity: O(1)
def max_sum1(arr, k):
    max_sum = 0
    for i in range(len(arr) - k + 1):
        current_sum = 0
        for j in range(i, i + k):
            current_sum += arr[j]
        max_sum = max(max_sum, current_sum)
    return max_sum

# Sliding window solution
# Time complexity: O(n)
# Space complexity: O(1)
def max_sum2(arr, k):
  max_sum = 0
  current_sum = 0
  for i in range(len(arr)):
    current_sum += arr[i]
    if i >= k - 1:
      max_sum = max(max_sum, current_sum)
      current_sum -= arr[i - k + 1]
  return max_sum

# is there a way to optimize the code above?
# yes, by using a deque. why? because we can remove the first element in O(1) time.


# testing
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
k = 3
print(max_sum1(arr, k))
print(max_sum2(arr, k))

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
k = 4
print(max_sum1(arr, k))
print(max_sum2(arr, k))