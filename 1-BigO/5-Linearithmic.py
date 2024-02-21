# Example 1
def example1(n):
    for i in range(n):
        print(i)
    j = 1
    while j <= n:
        print(j)
        j *= 2

# Example 2
def example2(n):
    i = 1
    while i <= n:
        print(i)
        i *= 2
    j = 1
    while j <= n:
        print(j)
        j *= 2

# Example 3: mergeSort
def merge_sort(arr):
    if len(arr) < 2:
        return arr
    middle = len(arr) // 2
    left_arr = arr[:middle]
    right_arr = arr[middle:]
    return merge(merge_sort(left_arr), merge_sort(right_arr))

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# Example 4: quickSort
def quick_sort(arr):
    if len(arr) < 2:
        return arr
    pivot = arr[0]
    left_arr = [x for x in arr[1:] if x < pivot]
    right_arr = [x for x in arr[1:] if x >= pivot]
    return quick_sort(left_arr) + [pivot] + quick_sort(right_arr)

# Example 5: heapSort
def heap_sort(arr):
    sorted_arr = []
    while arr:
        heapify(arr)
        sorted_arr.insert(0, arr.pop(0))
    return sorted_arr

def heapify(arr):
    start = (len(arr) - 2) // 2
    while start >= 0:
        sift_down(arr, start, len(arr) - 1)
        start -= 1

def sift_down(arr, start, end):
    root = start
    while root * 2 + 1 <= end:
        child = root * 2 + 1
        swap = root
        if arr[swap] < arr[child]:
            swap = child
        if child + 1 <= end and arr[swap] < arr[child + 1]:
            swap = child + 1
        if swap != root:
            arr[root], arr[swap] = arr[swap], arr[root]
            root = swap
        else:
            return

# Example 6: BST
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        # BST insertion logic
        pass

    def lookup(self, value):
        # BST search logic
        pass

# Example 6: Test BST
def test_bst():
    bst = BinarySearchTree()
    bst.insert(9)
    bst.insert(4)
    bst.insert(6)
    bst.insert(20)
    bst.insert(170)
    bst.insert(15)
    bst.insert(1)
    print(bst.root.value)
    print(bst.lookup(9))
    print(bst.lookup(4))
    print(bst.lookup(6))
    print(bst.lookup(20))
    print(bst.lookup(170))
    print(bst.lookup(15))
    print(bst.lookup(1))

print('example1:')
example1(10)
print('example2:')
example2(10)
print('mergeSort:', merge_sort([10, 24, 76, 73, 72, 1, 9]))
print('quickSort:', quick_sort([10, 24, 76, 73, 72, 1, 9]))
print('heapSort:', heap_sort([10, 24, 76, 73, 72, 1, 9]))
print('testBst:')
test_bst()
