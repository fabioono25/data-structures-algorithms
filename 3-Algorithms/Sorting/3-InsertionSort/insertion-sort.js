// Insertion Sort definition: A sorting algorithm where the values are inserted in the correct order
// Example: [5, 3, 4, 1, 2] ==> [3, 5, 4, 1, 2] ==> [3, 4, 5, 1, 2] ==> [1, 3, 4, 5, 2] ==> [1, 2, 3, 4, 5]

function insertionSort(array) {
  for (let i = 0; i < array.length; i++) {
    if (array[i] < array[0]) {
      // move number to the first position
      array.unshift(array.splice(i, 1)[0]);
    } else {
      // find where number should go
      for (let j = 1; j < i; j++) {
        if (array[i] > array[j - 1] && array[i] < array[j]) {
          // move number to the right spot
          array.splice(j, 0, array.splice(i, 1)[0]);
        }
      }
    }
  }
}

function insertionSort2(array) {
  for (let i = 1; i < array.length; i++) {
    let current = array[i];

    for (let j = i - 1; j >= 0 && array[j] > current; j--) {
      // if the current is lower than the min, we have a new min
      array[j + 1] = array[j];
      array[j] = current;
    }
  }
}

// is there a way to improve the insertion sort?
// yes, we can add a variable to check if the array is already sorted
// if it is, we can break the loop
// we can also add a variable to check if we made any swaps
// if we didn't, we can break the loop
// example:
function insertionSortOptimized(array) {
  for (let i = 1; i < array.length; i++) {
    let current = array[i];
    let noSwaps = true;

    for (let j = i - 1; j >= 0 && array[j] > current; j--) {
      // if the current is lower than the min, we have a new min
      array[j + 1] = array[j];
      array[j] = current;
      noSwaps = false;
    }

    if (noSwaps) break;
  }
}

const arr1 = [5, 3, 4, 1, 2];
insertionSort(arr1);
console.log(arr1);

const arr2 = [5, 3, 4, 1, 2];
insertionSort2(arr2);
console.log(arr2);

const arr3 = [5, 3, 4, 1, 2];
insertionSortOptimized(arr3);
console.log(arr3);