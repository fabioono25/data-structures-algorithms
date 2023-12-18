# integer reversion exercise. Example: 1234 -> 4321
# the input is an integer

# convert the integer to a string, reverse the string, and convert back to an integer
def reverse_integer(n):
    numstr = str(n)
    reversed_number = int(numstr[::-1])

    return reversed_number

# divide the number by 10 and get the remainder. Time complexity: O(n)
def reverse_integer2(n):
    reversed_number = 0
    remainder = 0
    while n > 0:
        remainder = n % 10
        reversed_number = reversed_number * 10 + remainder
        n = n // 10

    return reversed_number



# testing
print('input: 1234, output: ', reverse_integer(1234))
print('input: 1234, output: ', reverse_integer2(1234))