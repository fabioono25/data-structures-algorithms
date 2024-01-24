# given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.
# Example 1:  nums = [2, 7, 11, 15], target = 9 -> [0, 1]
# Example 2:  nums = [3, 2, 4], target = 6 -> [1, 2]

# Time complexity: O(n^2)
# Space complexity: O(1)
def two_sum(nums, target):
    for i, val in enumerate(nums):
        complement = target - val
        if complement in nums[i+1:]:
            return [i, nums.index(complement)]
    return []
  
# using two arrays
# Time complexity: O(n)
# Space complexity: O(n)


def two_sum2(nums, target):
    nums2 = nums.copy()
    nums2.sort()
    i = 0
    j = len(nums) - 1
    while i < j:
        if nums2[i] + nums2[j] == target:
            return [nums.index(nums2[i]), nums.index(nums2[j])]
        elif nums2[i] + nums2[j] < target:
            i += 1
        else:
            j -= 1
    return []

# using hash table
# Time complexity: O(n)
# Space complexity: O(n)


def two_sum3(nums, target):
    hash_table = {}

    for i in range(len(nums)):
        complement = target - nums[i]
        if complement in hash_table:
            return [hash_table[complement], i]
        hash_table[nums[i]] = i
    
    return []

# using hadh table
# Time complexity: O(n)
# Space complexity: O(n)


def two_sum4(nums, target):
    hash_table = {}

    for i, value in enumerate(nums):
        complement = target - value
        if complement in hash_table:
            return [hash_table[complement], i]
        hash_table[value] = i
    
    return []

# comparison between two_sum3 and two_sum4
# range() vs enumerate(): the most performatic is enumerate(), because it is a generator, it does not create a list in memory
# range, on the other hand, creates a list in memory


# testing
if __name__ == "__main__":
    # Driver Code
    nums = [2, 7, 11, 15]
    target = 9
    print(two_sum(nums, target))
    print(two_sum2(nums, target))
    print(two_sum3(nums, target))
    print(two_sum4(nums, target))
    nums = [3, 2, 4]
    target = 6
    print(two_sum(nums, target))
    print(two_sum2(nums, target))
    print(two_sum3(nums, target))
    print(two_sum4(nums, target))
    nums = [3, 2, 2]
    target = 6
    print(two_sum(nums, target))
    print(two_sum2(nums, target))
    print(two_sum3(nums, target))
    print(two_sum4(nums, target))