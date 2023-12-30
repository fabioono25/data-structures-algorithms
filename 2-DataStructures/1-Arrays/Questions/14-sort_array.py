# given an array which contain 1 to n elements, sort it in an efficient way without replace with 1 to n numbers.
# Example 1: [10, 7, 9, 2, 8, 3, 5, 4, 6, 1] -> [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Cyclic sort definition: it is a sorting technique that is based on the value of the elements and not on their index.

# Time complexity: O(n)
# Space complexity: O(1)
def sort(arr, n):
    # solve it
    return None

# using cyclic sort


# function to swap values
def swap(arr, first, second):
    temp = arr[first]
    arr[first] = arr[second]
    arr[second] = temp


if __name__ == "__main__":
    # Driver Code
    arr = [3, 2, 5, 6, 1, 4]
    n = len(arr)

    # function call
    sort(arr, n)

    # printing the answer
    for i in range(0, n):
        print(arr[i], end=" ")
