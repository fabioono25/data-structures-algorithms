# This is a review of Python basics for coding interviews:

# variables (dynamically typed):
from multiprocessing import heap
import math
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
s += ' Welcome to Python World!'  # a new string is created (immutability)
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

# List comprehension example:
squares = [i * i for i in range(10)]
print('squares=', squares)

print(25*'-')
print()

print("WORKING WITH CLASSES: ")


class Person:
    # constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hello(self):
        print('Hello, my name is', self.name,
              'and I am', self.age, 'years old')


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
# Careful. Why? See https://stackoverflow.com/questions/11720656/modulo-operation-with-negative-numbers
print('-10 % 3 = ', -10 % 3)

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


def myFunc(n, m):
    return n + m


print('myFunc(1, 2): ', myFunc(1, 2))


def outer(n, m):
    def inner(n, m):
        return n + m
    return inner(n, m)


print('outer(1, 2): ', outer(1, 2))

# Can modify objects but not reassign
# unless using nonlocal keyword


def double(arr, val):
    def helper():
        # Modifying array works
        for i, n in enumerate(arr):
            arr[i] *= 2

        # will only modify val in the helper scope
        # val *= 2

        # this will modify val outside helper scope
        nonlocal val
        val *= 2
    helper()
    print(arr, val)


nums = [1, 2]
val = 3
double(nums, val)

print(25*'-')
print()

print("WORKING WITH ARRAYS: ")

# arrays are called lists in Python (dynamic)
arr = [1, 2, 3, 4, 5]
print('arr=', arr)

# using as stack
arr.append(6)
arr.append(7)
arr.append(8)
arr.pop()
print('arr=', arr)
arr.insert(1, 22)
print('arr=', arr)
print('arr[-1]', arr[-1])
print('arr[-2:]', arr[-2:])

# slicing an array
print('arr[2:4]', arr[2:4])  # last index non-inclusive
print('arr[2:20]', arr[2:20])  # last index non-inclusive

# initialize arr of size n with default value of 1
n = 5
arr = [1] * n
print('arr=', arr)
print('len(arr)=', len(arr))

# unpacking
a, b, c = [1, 2, 3]
print('a=', a, 'b=', b, 'c=', c)
# a, b = [1, 2, 3]
# print('a=', a, 'b=', b) error

nums = [1, 2, 3]

# using index to loop
for i in range(len(nums)):
    print('nums[i]=', nums[i])

# using index and value
for i, n in enumerate(nums):
    print('i=', i, 'n=', n)

# loop and unpacking
nums1 = [1, 2, 3]
nums2 = [4, 5, 6]
for n1, n2 in zip(nums1, nums2):
    print('n1=', n1, 'n2=', n2)

nums1.reverse()
print('nums1=', nums1)
nums1.sort()
print('nums1=', nums1)
nums1.sort(reverse=True)
print('nums1=', nums1)

arr = ["bob", "alice", "jane", "doe"]
arr.sort()
print('arr=', arr)

# custom sort by length of string
arr.sort(key=len)
print('arr=', arr)

# array comprehension
arr = [i for i in range(4)]
print('arr=', arr)

# 2-D lists
arr = [[0] * 4 for i in range(4)]
print(arr)
print(arr[0][0], arr[3][3])

print(25*'-')
print()

print("WORKING WITH QUEUES: ")

from collections import deque

queue = deque()
queue.append(1)
queue.append(2)
queue.append(3)
print('queue=', queue)
print('queue.popleft()=', queue.popleft())
print('queue.popleft()=', queue.popleft())
print('queue.appendleft()=', queue.appendleft(11))
print('queue=', queue)
queue.pop()
print('queue=', queue)


print(25*'-')
print()

print("WORKING WITH HASHSETS: ")

mySet = set()
mySet.add(1)
mySet.add(2)
mySet.add(3)
mySet.add(3)
print('mySet=', mySet)
print('len(mySet)=', len(mySet))

print('1 in mySet=', 1 in mySet)
print('4 in mySet=', 4 in mySet)

mySet.remove(1)
print('mySet=', mySet)

# set comprehension
mySet = {i for i in range(4)}
print('mySet=', mySet)

print(25*'-')
print()

print("WORKING WITH HASHMAPS: ")


print(25*'-')
print()

print("WORKING WITH TUPLES: ")

print(25*'-')
print()

print("WORKING WITH HEAPS: ")
