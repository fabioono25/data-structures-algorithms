# given an array, cyclically rotate the array clockwise by one.
# Example 1: [1,2,3,4,5] -> [5,1,2,3,4]
# Example 2: [9,8,7,6,4,2,1,3] -> [3,9,8,7,6,4,2,1]

# Time complexity: O(n)
# Space complexity: O(1)
def rotate(arr, n):
    # solve it
    return None

if __name__ == "__main__":
  # Driver function
  arr = [1, 2, 3, 4, 5]
  n = len(arr)
  print("Given array is")
  for i in range(0, n):
      print(arr[i], end=' ')

  rotate(arr, n)

  print("\nRotated array is")
  for i in range(0, n):
      print(arr[i], end=' ')
