// heap sort definition: A sorting algorithm where we first build a heap and then swap the first and last elements and then heapify down.
// example: [5, 3, 4, 1, 2] ==> [5, 3, 4, 1, 2] ==> [4, 3, 2, 1, 5] ==> [3, 1, 2, 4, 5] ==> [2, 1, 3, 4, 5] ==> [1, 2, 3, 4, 5]

function heapSort(array) {
  // build the heap
  for (let i = Math.floor(array.length / 2); i >= 0; i--) {
    heapifyDown(array, i, array.length);
  }

  // swap the first and last elements and heapify down
  for (let i = array.length - 1; i > 0; i--) {
    swap(array, 0, i);
    heapifyDown(array, 0, i);
  }

  return array;
}

function heapifyDown(array, index, length) {
  let left = 2 * index + 1;
  let right = 2 * index + 2;
  let largest = index;

  // if the left child is larger than the parent
  if (left < length && array[left] > array[largest]) {
    largest = left;
  }

  // if the right child is larger than the parent
  if (right < length && array[right] > array[largest]) {
    largest = right;
  }

  // if the largest is not the parent
  if (largest !== index) {
    swap(array, index, largest);
    heapifyDown(array, largest, length);
  }
}

function swap(array, index1, index2) {
  let temp = array[index1];

  array[index1] = array[index2];
  array[index2] = temp;
}

const numbers = [5, 3, 4, 1, 2];
console.log(heapSort(numbers));
