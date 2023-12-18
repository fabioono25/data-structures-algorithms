# anagram exercise. Example: 'dog' and 'god' are anagrams
# example2: 'clint eastwood' and 'old west action'

# Using a dictionary. Time complexity: O(n)
def is_anagram(str1, str2):
    if len(str1) != len(str2):
        return False

    ret = {}

    for letter in str1:
        if letter in ret:
            ret[letter] += 1
        else:
            ret[letter] = 1

    for letter in str2:
        if letter in ret:
            ret[letter] -= 1

    return all(value == 0 for value in ret.values())


# using sorting. Time complexity: O(n log n)
def is_anagram2(str1, str2):
    if len(str1) != len(str2):
        return False

    return sorted(str1) == sorted(str2)

# testing
print('input: dog, god, output: ', is_anagram('dog', 'god'))
print('input: dog, god, output: ', is_anagram2('dog', 'god'))