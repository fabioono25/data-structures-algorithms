# This is a review of Python basics for coding interviews:

# variables (dynamically typed):
print("WORKING WITH VARIABLES: ")

n = 300
print('n=', n)

n = 'foo'
print('n=', n)

# multiple assignments:
n, m, z = 122, 'Hello', 3.14
print('n=', n, 'm=', m, 'z=', z)

# Increment
n += 1
print('n=', n)

# Representation of null in Python
n = None
print('n=', n)

print(25*'-')
print()

# Strings: are immutable
print("WORKING WITH STRINGS: ")

# strings
s = 'Hello World!'
print('s=', s)

# length
print('len(s)=', len(s))

# slicing
print('s[0]=', s[0])
print('s[1:]=', s[1:])
print('s[1:5]=', s[1:5])
print('s[:3]=', s[:3])
# last element
print('s[-1]=', s[-1])
print('s[:-3]=', s[:-3])
# 3 last elements
print('s[-3:]=', s[-3:])
# reverse
print('s[::-1]=', s[::-1])
# concatenation
s += ' Welcome to Python World!' # a new string is created (immutability)
print('s=', s)

print('Converting values: ', int('1') + 233 + int('314'))
# converting to string
print('Converting to string: ', str(1) + '23' + str(314))

# ASCII values
print('ASCII value of A: ', ord('A'))
print('ASCII value of a: ', ord('a'))

# combine array of strings
print('  '.join(['Hello', 'World', '!']))

print(25*'-')
print()

print("WORKING WITH CONDITIONALS: ")
n = 1
if n < 0:
    print('n is negative')
elif n > 0:
    print('n is positive')
else:
    print('n is zero')

n, m = 1, 2
if ((n > 2 and n != m) or n == m):
    print('if statement')

print(25*'-')
print()

print("WORKING WITH LOOPS: ")
