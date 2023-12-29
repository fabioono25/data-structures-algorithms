# given a non-empty array of integers, every element appears three times except for one. Find that single one.
# Note: your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
# Example 1: [2,2,3,2] -> 3
# Example 2: [0,1,0,1,0,1,99] -> 99

# Time complexity: O(n)
# Space complexity: O(n)
def single_numbers(num):
    dict = {}

    for n in num:
        if n in dict:
            dict[n] += 1
        else:
            dict[n] = 1

    for key, value in dict.items():
        if value == 1:
            return key


# test cases
print('Input: [2,2,3,2] \nOutput: ', single_numbers([2, 2, 3, 2]))
print('Input: [0,1,0,1,0,1,99] \nOutput: ',
      single_numbers([0, 1, 0, 1, 0, 1, 99]))
print('Input: [1] \nOutput: ', single_numbers([1]))
print('Input: [1,1,1,2] \nOutput: ', single_numbers([1, 1, 1, 2]))
print('Input: [1,1,1,2,2,2,3] \nOutput: ',
      single_numbers([1, 1, 1, 2, 2, 2, 3]))
