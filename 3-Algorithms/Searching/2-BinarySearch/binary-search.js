// Binary Search definition: find the middle element in the array, check if it's the element we're looking for, if not, check if the element we're looking for is less than or greater than the middle element, and then repeat the process with the left or right half of the array
// time complexity: O(log n) - logarithmic time
// space complexity: O(1) - constant space

function BinarySearch(array, item) {
  let left = 0;
  let right = array.length - 1;
  let middle = Math.floor((left + right) / 2);

  while (array[middle] !== item && left <= right) {
    if (item < array[middle]) right = middle - 1;
    else left = middle + 1;
    middle = Math.floor((left + right) / 2);
  }
  return array[middle] === item ? middle : -1;
}

const numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
console.log('binary search: ', numbers);
console.log(BinarySearch(numbers, 1));
console.log(BinarySearch(numbers, 5));
