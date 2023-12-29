# given an array nums and value val, remove all instances of that value in-place and return the new length
# do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory
# the order of elements can be changed. It doesn't matter what you leave beyond the new length
# Example 1: nums = [3,2,2,3], val = 3 -> [2,2] - length: 2
# Example 2: nums = [0,1,2,2,3,0,4,2], val = 2 -> [0,1,3,0,4] - length: 5

# Time complexity: O(n)
# Space complexity: O(1)

def remove_element(nums, val):
  index = 0

  for i in range(len(nums)):
    if nums[i] != val:
      nums[index] = nums[i]
      index += 1

  return index

# test cases
print('Input: [3,2,2,3], 3 \nOutput: ', remove_element([3,2,2,3], 3))
print('Input: [0,1,2,2,3,0,4,2], 2 \nOutput: ', remove_element([0,1,2,2,3,0,4,2], 2))
print('Input: [1], 1 \nOutput: ', remove_element([1], 1))
print('Input: [1,1,1,2], 1 \nOutput: ', remove_element([1,1,1,2], 1)) 