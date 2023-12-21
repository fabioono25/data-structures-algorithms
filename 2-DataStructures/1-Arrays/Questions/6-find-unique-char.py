# Given a string, find the first non-repeating character in it and return its index. If it doesn't exist, return -1.
# Examples:
# s = "leetcode" -> return 0.
# s = "loveleetcode" -> return 2.
# Note: You may assume the string contains only lowercase English letters.

# Solution 1: Using a dictionary. Time complexity: O(N), Space complexity: O(N)
from collections import deque


def first_unique_char(s):
    # create a dictionary to store the frequency of each character
    freq = {}

    # iterate to each character and save the index
    for i in range(len(s)):
        if s[i] in freq:
            freq[s[i]] = -1
        else:
            freq[s[i]] = i

    # loop through the freq dictionary
    for key, value in freq.items():
        if value != -1:
            return value

    # loop through the string and check if the frequency of each character is 1
    # for i in range(len(s)):
    #   if freq[s[i]] == 1:
    #     return i
    return -1


# Solution 2: Using a queue. Time complexity: O(N), Space complexity: O(N)


def first_unique_char2(s):
    # create a dictionary to store the frequency of each character
    freq = {}
    for char in s:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1

    # create a queue to store the index of the first unique character
    queue = deque()
    for i in range(len(s)):
        if freq[s[i]] == 1:
            queue.append(i)

    # return the index of the first unique character
    return queue[0] if queue else -1


# testing
print("Input: leetcode", "Output:", first_unique_char("leetcode"))
print("Input: loveleetcode", "Output:", first_unique_char("loveleetcode"))
print("Input: leetcode", "Output:", first_unique_char2("leetcode"))
print("Input: loveleetcode", "Output:", first_unique_char2("loveleetcode"))
