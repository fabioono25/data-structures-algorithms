# O(1)/Constant Time Complexity: The time complexity of an algorithm is said to be constant time if the time taken by the algorithm is the same for all inputs of size n.

# in the example below, the idea is to show how the time complexity of the algorithm is constant time for all inputs of size n.
# no matter the size of the input, the time taken by the algorithm will always be the same.
def find_first(array):
    return array[0]


def find_last(array):
    return array[-1]


def is_even_or_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"


def is_even_or_odd2(number):
    return "Even" if number % 2 == 0 else "Odd"

# nth meaning: 3rd, 4th, 5th, etc


def find_nth(array, n):
    return array[n - 1]


def first_and_last(array):
    return [array[0], array[-1]]


def get_value_for_key(hash_map, key):
    return hash_map.get(key)


def get_value_for_key_2(dictionary, key):
    return dictionary.get(key, "Key not found")


def swap_variables(a, b):
    a = a + b
    b = a - b
    a = a - b
    return [a, b]


def swap_variables2(a, b):
    a, b = b, a
    return [a, b]


def get_element_at_index(arr, index):
    if 0 <= index < len(arr):
        return arr[index]
    else:
        return "Index out of bounds"


def get_element_at_index2(arr, index):
    return arr[index] if 0 <= index < len(arr) else "Index out of bounds"


print("First of [1, 2, 3, 4, 5, 6]: ", find_first([1, 2, 3, 4, 5, 6]))
print("Last of [1, 2, 3, 4, 5, 6]: ", find_last([1, 2, 3, 4, 5, 6]))
print(25*"-")
print("Even or Odd of 2: ", is_even_or_odd(2))
print("Even or Odd of 3: ", is_even_or_odd(3))
print("Even or Odd of 2: ", is_even_or_odd2(2))
print("Even or Odd of 3: ", is_even_or_odd2(3))
print(25*"-")
print("Nth 3 of [1, 2, 3, 4, 5, 6]: ", find_nth([1, 2, 3, 4, 5, 6], 3))
print("Nth 2 of char of 'Hello': ", find_nth("Hello", 2))
print(25 * "-")
print("First and Last of [1, 2, 3, 4, 5, 6]: ",
      first_and_last([1, 2, 3, 4, 5, 6]))
print(25 * "-")

# key-value pair are also known as dictionary. It is implemented as a hash map in Python.
dict = {
    "key1": "value1",
    "key2": "value2",
    "key3": "value3",
}
print(" Hash Map is ", dict)
print("Value of 'key1': ", get_value_for_key(dict, "key1"))
print("Value of 'key22': ", get_value_for_key(dict, "key22"))  # None
print("Get Element from [1, 2, 3, 4, 5, 6] at Index 3: ",
      get_element_at_index([1, 2, 3, 4, 5, 6], 3))
print("Get Element from [1, 2, 3, 4, 5, 6] at Index 10: ", get_element_at_index2(
    [1, 2, 3, 4, 5, 6], 10))  # Index out of bounds
print(25 * "-")

print("Swap Variables 1 and 2: ", swap_variables(1, 2))
print("Swap Variables 1 and 2: ", swap_variables2(1, 2))

print(25 * "-")
