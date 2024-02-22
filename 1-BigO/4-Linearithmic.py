# O(n log n) Linearithmic/Loglinear Time Complexity: The time complexity of an algorithm is said to be linearithmic if the time taken by the algorithm is
# directly proportional to the size of the input and the logarithm of the size of the input.
# Pros:
# 1. Efficient for large inputs: Linearithmic time algorithms are efficient for large input sizes since the time taken increases linearly with the input size and logarithmically with the input size.
# 2. Scalable: Linearithmic time algorithms can handle large inputs without a significant increase in execution time, making them scalable.
# 3. Flexibility: Linearithmic time complexity can be used to solve a wide range of problems and is suitable for a variety of applications.
# 4. Simplifies algorithm analysis: Linearithmic time complexity simplifies the analysis of algorithms and allows for easier comparison between different algorithms.
# Cons:
# 1. Limited performance: Linearithmic time algorithms may not be able to achieve the same level of performance as algorithms with lower time complexity.
# 2. Inefficient for small inputs: Linearithmic time algorithms may be less efficient for small input sizes since the time taken increases with the input size.
# 3. Complexity: Linearithmic time algorithms may be more complex to implement and analyze compared to algorithms with lower time complexity.
# 4. Limited applicability: Linearithmic time algorithms may not be suitable for all problems and may not be efficient for small input sizes.

# Example 1: mergeSort. The time complexity of merge sort is O(n log n)
# why: the time complexity of merge sort is O(n log n) because it divides the input array into two halves, recursively sorts them, and then merges the sorted halves.
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

# Example 2: quickSort. The time complexity of quick sort is O(n log n)
# why: the time complexity of quick sort is O(n log n) because it divides the input array into two halves, recursively sorts them, and then merges the sorted halves.
def quick_sort(arr):
    if len(arr) < 2:
        return arr
    pivot = arr[0]
    left_arr = [x for x in arr[1:] if x < pivot]
    right_arr = [x for x in arr[1:] if x >= pivot]
    return quick_sort(left_arr) + [pivot] + quick_sort(right_arr)

# Example 3: heapSort. The time complexity of heap sort is O(n log n)
# why: the time complexity of heap sort is O(n log n) because it builds a max heap, swaps the root with the last element, and then heapifies the remaining elements.
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


print('mergeSort:', merge_sort([10, 24, 76, 73, 72, 1, 9]))
print('quickSort:', quick_sort([10, 24, 76, 73, 72, 1, 9]))
print('heapSort:', heap_sort([10, 24, 76, 73, 72, 1, 9]))
print('testBst:')
test_bst()
