# Arrays definition: it's a collection of items stored at contiguous memory locations.
# The idea is to store multiple items of the same type together.
# This makes it easier to calculate the position of each element by simply adding an offset to a base value,
# i.e., the memory location of the first element of the array (generally denoted by the name of the array).
# The base value is index 0 and the difference between the two indexes is the offset.
# Time complexity: O(1) for access, O(n) for search, O(n) for insertion, O(n) for deletion
# Space complexity: O(n)

# Python lists are arrays, but they are not fixed in size.
# if you want to use a real array in Python, you should use the array module. Problem: it only supports a single datatype.
# or you can use the NumPy package, which is a much better alternative. Problem: it's not a part of the standard Python library.

my_list = [1, 5, 10, 4, "hello", 3.14, True, [1, 2, 3]]
print(my_list)
print("Length: ", len(my_list))

my_list[0] = 212
for item in my_list:
    print(item)

# del operator to delete an item at a specific index. Time complexity: O(n)
del my_list[0]
print(my_list)
print("Length: ", len(my_list))

# append() to add an item at the end of the list. Time complexity: O(1)
my_list.append("new item")
print(my_list)

# print the last 2 items
print(my_list[-2:])
print("Length: ", len(my_list))

print(25*"-")

# insert() to add an item at a specific index. Time complexity: O(n)
my_list.insert(2, "new item")
print(my_list)
print("Length: ", len(my_list))

list1 = [1, 2, 3]
list2 = [4, 5, 6]

result = list1 + list2  # combine the two items. Time complexity: O(n)
print(result)

# add the second list to the first one. Time complexity: O(n)
list1.extend(list2)
list1.append("test")
print(list1)
print(list2)

result2 = list1.copy()  # copy the list. Time complexity: O(n). Space complexity: O(n)
print(result2)

# remove the first occurrence of the item. Time complexity: O(n)
list1.remove(2)
list1.pop()  # remove the last item. Time complexity: O(1)
print(list1)

list1.reverse()  # reverse the list. Time complexity: O(n)
print(list1)
list1.sort()  # sort the list. Time complexity: O(n log n)
print(list1)

print(25*"-")

# list comprehension: a concise way to create lists.
# It consists on creating a new list from an existing one, based on a condition.
# Syntax: [expression for item in list if condition]

numbers = [1, -6, 3, 5, -2, 8, 0, -1]

new_list = [x for x in numbers if x > 0]

print("newList: ", new_list)

new_list.clear()
for num in numbers:
    if num % 2 == 0:
        new_list.append(num)

print("newList: ", new_list)

new_list.clear()
new_list = [num for num in numbers if num % 2 == 0]
print("newList: ", new_list)
