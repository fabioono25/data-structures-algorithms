# Rabin-Karp Substring Search definition: it is a string searching algorithm that uses hashing to find any one of a set of pattern strings in a text.
# The problem with brutal-force is that it takes O(mn) time in the worst case. Rabin-Karp algorithm takes O(m+n) time in the worst case.
# Compare strings in O(1) time? Hashing! We transform multiple characters into a single value and compare the values instead of the characters.
# 