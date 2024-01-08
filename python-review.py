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

n = 0
while n < 5:
    print('Value of n is', n)
    n += 1


for i in range(5):
    print('Value of i is', i)

for i in range(3, 8):
    print('Value of i is', i)


for i in range(10, 1, -2):
    print('Value of i is', i)

print(25*'-')
print()

print("WORKING WITH CLASSES: ")
class Person:
    # constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hello(self):
        print('Hello, my name is', self.name, 'and I am', self.age, 'years old')

person = Person('John', 12)
person.say_hello()


print(25*'-')
print()

print("WORKING WITH MATH: ")
print(' 5 / 2 = ', 5 / 2)
print(' 5 // 2 = ', 5 // 2)
print(' -3 // 2 = ', -3 // 2)
print('-3 / 2 = ', -3 / 2)
print('int(-3 / 2) = ', int(-3 / 2))
print(' 5 % 2 = ', 5 % 2)
print('-10 % 3 = ', -10 % 3) # Careful. Why? See https://stackoverflow.com/questions/11720656/modulo-operation-with-negative-numbers

import math
from multiprocessing import heap
print('math.fmod(-10, 3) = ', math.fmod(-10, 3))

print('math.floor(3 / 2): ', math.floor(3 / 2))
print('math.ceil(3 / 2): ', math.ceil(3 / 2))
print('math.sqrt(2): ', math.sqrt(2))
print('math.pow(2, 3): ', math.pow(2, 3))

# print min int
print('min int: ', -2**31)

# print max int
print('max int: ', 2**31 - 1)

# Python numbers are infinite: they never overflow
print('max int + 1000: ', 2**31 + 9999)

# But still less than infinity
print(math.pow(2, 200) < float("inf"))

print(25*'-')
print()

print("WORKING WITH FUNCTIONS: ")


print(25*'-')
print()

print("WORKING WITH ARRAYS: ")


print(25*'-')
print()

print("WORKING WITH QUEUES: ")


print(25*'-')
print()

print("WORKING WITH HASHSETS: ")

print(25*'-')
print()

print("WORKING WITH HASHMAPS: ")


print(25*'-')
print()

print("WORKING WITH TUPLES: ")

print(25*'-')
print()

print("WORKING WITH HEAPS: ")
