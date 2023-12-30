# given an unsorted array of integers, sort the array into a wave array.
# An array arr[0..n-1] is expressed as arr[0] >= arr[1] <= arr[2] >= arr[3] <= arr[4] >= …..
# Example 1: [1,2,3,4] -> [2,1,4,3]
# Example 2: [1,2,3,4,5] -> [2,1,4,3,5]

# Time complexity: O(n)
# Space complexity: O(1)
def sortInWave(arr, n):
    # solve it
    return None

if __name__ == "__main__":
  # testing
  arr = [10, 90, 49, 2, 1, 5, 23]
  print("Before sort: ", arr)

  sortInWave(arr, len(arr))

  for i in range(0,len(arr)):
      print (arr[i],end=" ")