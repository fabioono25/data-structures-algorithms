// Bubble Sort definition: A sorting algorithm where the largest values bubble up to the top
// Example: [5, 3, 4, 1, 2] ==> [3, 4, 1, 2, 5] ==> [3, 1, 2, 4, 5] ==> [1, 2, 3, 4, 5]

function bubbleSort(array) {
  for (let i = 0; i < array.length; i++) {
    // console.log('i', i);
    for (let j = 0; j < array.length; j++) {
      // console.log('j', j);
      if (array[j] > array[j + 1]) {
        // swap numbers
        let temp = array[j];
        array[j] = array[j + 1];
        array[j + 1] = temp;
      }
    }
  }
}

// is there a way to improve the bubble sort?
// yes, we can add a variable to check if the array is already sorted
// if it is, we can break the loop
// we can also add a variable to check if we made any swaps
// if we didn't, we can break the loop
// this way we can improve the bubble sort
function bubbleSortOptimized(array) {
  let noSwaps;
  for (let i = array.length; i > 0; i--) {
    // console.log('i', i);
    noSwaps = true;
    for (let j = 0; j < i - 1; j++) {
      // console.log('j', j);
      if (array[j] > array[j + 1]) {
        // swap numbers
        let temp = array[j];
        array[j] = array[j + 1];
        array[j + 1] = temp;
        noSwaps = false;
      }
    }

    if (noSwaps) break;
  }
}

const numbers = [5, 3, 4, 1, 2];
bubbleSort(numbers);
console.log(numbers);

const numbers2 = [5, 3, 4, 1, 2];
bubbleSortOptimized(numbers2);
console.log(numbers2);
