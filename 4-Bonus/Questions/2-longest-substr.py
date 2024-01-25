# given a string s, find the length of the longest substring without repeating characters.
# example: s = "abcabcbb" -> 3
# example: s = "bbbbb" -> 1
# example: s = "pwwkew" -> 3

# using hash table (recommended - more concise)
# Time complexity: O(n)
# Space complexity: O(n)
def longest_substring(s):
    hash_table = {}
    max_length = 0
    start = 0

    for i, value in enumerate(s):
        if value in hash_table:
            start = max(start, hash_table[value] + 1)
        hash_table[value] = i
        max_length = max(max_length, i - start + 1)

    return max_length

# using sliding window
def longest_substring2(s):
    max_length = 0
    start = 0
    hash_table = {}

    for i, value in enumerate(s):
        if value in hash_table and start <= hash_table[value]:
            start = hash_table[value] + 1
        else:
            max_length = max(max_length, i - start + 1)
        hash_table[value] = i

    return max_length
  
# another way of using sliding window
def longest_substring3(s):
    n = len(s)
    max_len = 0
    start = 0
    char_dict = {}
    for end in range(n):
        if s[end] in char_dict:
            start = max(start, char_dict[s[end]] + 1)
        char_dict[s[end]] = end
        max_len = max(max_len, end - start + 1)
    return max_len

#testing
s = "abcabcbb"
print("Input: ", s, ". Result: ", longest_substring(s))
print("Input: ", s, ". Result: ", longest_substring2(s))
print("Input: ", s, ". Result: ", longest_substring3(s))

s = "bbbbb"
print("Input: ", s, ". Result: ", longest_substring(s))
print("Input: ", s, ". Result: ", longest_substring2(s))
print("Input: ", s, ". Result: ", longest_substring3(s))

s = "pwwkew"
print("Input: ", s, ". Result: ", longest_substring(s))
print("Input: ", s, ". Result: ", longest_substring2(s))
print("Input: ", s, ". Result: ", longest_substring3(s))
