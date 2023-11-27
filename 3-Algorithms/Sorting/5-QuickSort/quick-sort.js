// quick sort definition: A sorting algorithm where we pick a pivot and put all the elements smaller than the pivot to the left and all the elements greater than the pivot to the right
// example: [5, 3, 4, 1, 2] ==> [3, 4, 1, 2] [5] ==> [1, 2] [3, 4] [5] ==> [1] [2] [3] [4] [5] ==> [1, 2, 3, 4, 5]

function quickSort(array, left = 0, right = array.length - 1) {
  // base case
  if (left < right) {
    // get the pivot index
    let pivotIndex = pivot(array, left, right);

    // sort the left
    quickSort(array, left, pivotIndex - 1);

    // sort the right
    quickSort(array, pivotIndex + 1, right);
  }

  return array;
}

function pivot(array, start = 0, end = array.length - 1) {
  // grab the pivot from the start
  let pivot = array[start];
  let swapIndex = start;

  // loop through the array
  for (let i = start + 1; i <= end; i++) {
    // if the pivot is greater than the current element, increment the pivot index and swap
    if (pivot > array[i]) {
      swapIndex++;
      swap(array, swapIndex, i);
    }
  }

  // swap the pivot with the swap index
  swap(array, start, swapIndex);

  return swapIndex;
}

function swap(array, index1, index2) {
  let temp = array[index1];

  array[index1] = array[index2];
  array[index2] = temp;
}

const numbers = [5, 3, 4, 1, 2];
console.log(quickSort(numbers));
