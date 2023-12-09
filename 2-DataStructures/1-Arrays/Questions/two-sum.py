# two sum: given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# example1: nums = [2, 7, 11, 15], target = 9 -> [0, 1]
# example2: nums = [3, 2, 4], target = 6 -> [1, 2]

# brute force solution: Time complexity: O(n^2). Space complexity: O(1)
def two_sum(nums, target):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[j] == target - nums[i]:
                return [i, j]

# two-pass hash table: Time complexity: O(n). Space complexity: O(n)
def two_sum2(nums, target):
    hash_table = {}
    for i in range(len(nums)):
        hash_table[nums[i]] = i

    for i in range(len(nums)):
        complement = target - nums[i]
        if complement in hash_table:
            return [i, hash_table[complement]]

# one-pass hash table: Time complexity: O(n). Space complexity: O(n)
def two_sum3(nums, target):
    hash_table = {}
    for i in range(len(nums)):
        complement = target - nums[i]
        if complement in hash_table:
            return [hash_table[complement], i]
        hash_table[nums[i]] = i

# test

nums = [2, 7, 11, 15]
target = 9

print("nums: ", nums)
print("target: ", target, "\n")
print("Brutal Force: ", two_sum(nums, target))
print("Two-pass Hash Table: ", two_sum2(nums, target))
print("One-pass Hash Table: ", two_sum3(nums, target), "\n")

print(25*"-")

nums = [3, 2, 4]
target = 6

print("nums: ", nums)
print("target: ", target, "\n")
print("Brutal Force: ", two_sum(nums, target))
print("Two-pass Hash Table: ", two_sum2(nums, target))
print("One-pass Hash Table: ", two_sum3(nums, target), "\n")

print(25*"-")

nums = [3, 3, 4, 3]
target = 6

print("nums: ", nums)
print("target: ", target, "\n")
print("Brutal Force: ", two_sum(nums, target))
print("Two-pass Hash Table: ", two_sum2(nums, target))
print("One-pass Hash Table: ", two_sum3(nums, target))

print(25*"-")