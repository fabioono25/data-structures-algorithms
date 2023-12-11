# palindrome: a string that reads the same forward and backward
# example: "madam" is a palindrome
# example: "abba" is a palindrome

# Solution 1: Using a loop. Time complexity: O(N), Space complexity: O(1)
def palindrome1(str):
    for i in range(len(str) // 2):
        if str[i] != str[len(str) - i - 1]:
            return False
    return True

# Solution 2: Using recursion. Time complexity: O(N), Space complexity: O(N)


def palindrome2(str):
    if len(str) == 0:
        return True
    if str[0] != str[-1]:
        return False
    return palindrome2(str[1:-1])

# Solution 3: Using the built-in reverse() method. Time complexity: O(N), Space complexity: O(1)


def palindrome3(str):
    return str == str[::-1]


# Test cases
print("Input: madam", palindrome1("madam"))  # True
print("Input: abab", palindrome1("abab"))  # False
print("Input: ''",palindrome1(""))  # True
print(25*"-")
print("Input: madam", palindrome2("madam"))  # True
print("Input: abab",palindrome2("abab"))  # False
print("Input: ''",palindrome2(""))  # True
print(25*"-")
print("Input: madam", palindrome3("madam"))  # True
print("Input: abab",palindrome3("abab"))  # False
print("Input: ''",palindrome3(""))  # True
