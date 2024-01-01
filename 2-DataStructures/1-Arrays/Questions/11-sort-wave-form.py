# given an unsorted array of integers, sort the array into a wave array.
# An array arr[0..n-1] is expressed as arr[0] >= arr[1] <= arr[2] >= arr[3] <= arr[4] >= …..
# Example 1: [1,2,3,4] -> [2,1,4,3]
# Example 2: [10, 5, 6, 3, 2, 20, 100, 80] -> [10, 5, 6, 2, 20, 3, 100, 80]

# Time complexity: O(n)
# Space complexity: O(1)
# Suggestion to approach this problem: sort the array first, then swap adjacent elements.
def sortInWave(arr, n):
    # verify if the array is empty
    if n == 0 or n == 1:
        return arr

    # sort the array first
    arr.sort()

    # swap adjacent elements
    for i in range(0, n-1, 2):
        arr[i], arr[i+1] = arr[i+1], arr[i]

    # solve it
    return arr


if __name__ == "__main__":
    # testing
    arr = [1, 2, 3, 4]
    print("Before sort: ", arr)
    sortInWave(arr, len(arr))
    print("After sort: ", arr)
    print(25*"-")

    arr = [10, 90, 49, 2, 1, 5, 23]
    print("Before sort: ", arr)

    sortInWave(arr, len(arr))
    print("After sort: ", arr)
