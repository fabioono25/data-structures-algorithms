# Brute-force substring search algorithm
# inputs: text, pattern
# output: index of pattern in text
# example: abcdeefabcabcd -> abcd -> 9
# example: abcdeefabcabcd -> abce -> -1
# example: text = "abacadabrabracabracadabrabrabracad", pattern = "abracadabra" -> 14

# Time complexity: O(mn)
# Space complexity: O(1)
def naive_search(text, pattern):
  m = len(pattern)
  n = len(text)

  for i in range(n-m+1):
    for j in range(m):
      if text[i+j] != pattern[j]:
        break

      if j == m-1:
        return i
  return -1

print(naive_search("abcdeefabcabcd", "abcd")) # expected: 0
print(naive_search("abcdeefabcabcd", "abce")) # expected: -1
print(naive_search("abacadabrabracabracadabrabrabracad", "abracadabra")) # expected: 14
