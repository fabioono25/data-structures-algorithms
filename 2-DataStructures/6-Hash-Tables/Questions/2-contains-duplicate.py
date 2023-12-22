# Given an array, find if the array contains any duplicates
# ex: [1,2,3,1] -> True
# ex: [1,2,3,4] -> False
# ex: [1,1,1,3,3,4,3,2,4,2] -> True

# Solution 1: Brute Force
# Time Complexity: O(n^2)
# Space Complexity: O(1)
def containsDuplicate1(nums):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] == nums[j]:
                return True
    return False

# Solution 2: Sorting
# Time Complexity: O(nlogn)
# Space Complexity: O(1)
def containsDuplicate2(nums):
    nums.sort()
    for i in range(len(nums)-1):
        if nums[i] == nums[i+1]:
            return True
    return False

# Solution 3: Hash Table
def containsDuplicate3(nums):
    freq = {}
    for num in nums:
        if num in freq:
            return True
        else:
            freq[num] = 1
    return False

# Solution 4: Set
def containsDuplicate4(nums):
    return len(nums) != len(set(nums))

# tests
nums = [1,2,3,1]
print('Input: ', nums)
print('Solution 1: Brute Force')
print('Output: ', containsDuplicate1(nums))
print(25*'-')
print('Solution 2: Sorting')
print('Output: ', containsDuplicate2(nums))
print(25*'-')
print('Solution 3: Hash Table')
print('Output: ', containsDuplicate3(nums))
print(25*'-')
print('Solution 4: Set')
print('Output: ', containsDuplicate4(nums))
print(25*'#')
nums = [1,2,3,4]
print('Input: ', nums)
print('Solution 1: Brute Force')
print('Output: ', containsDuplicate1(nums))
print(25*'-')
print('Solution 2: Sorting')
print('Output: ', containsDuplicate2(nums))
print(25*'-')
print('Solution 3: Hash Table')
print('Output: ', containsDuplicate3(nums))
print(25*'-')
print('Solution 4: Set')
print('Output: ', containsDuplicate4(nums))
print(25*'#')
nums = [1,1,1,3,3,4,3,2,4,2]
print('Input: ', nums)
print('Solution 1: Brute Force')
print('Output: ', containsDuplicate1(nums))
print(25*'-')
print('Solution 2: Sorting')
print('Output: ', containsDuplicate2(nums))
print(25*'-')
print('Solution 3: Hash Table')
print('Output: ', containsDuplicate3(nums))
print(25*'-')
print('Solution 4: Set')
print('Output: ', containsDuplicate4(nums))
print(25*'#')
