//  merge sort definition: A sorting algorithm where we split the array in half and sort each half
// example: [5, 3, 4, 1, 2] ==> [5, 3, 4] [1, 2] ==> [5, 3] [4] [1] [2] ==> [5] [3] [4] [1] [2] ==> [3, 5] [1, 4] [2] ==> [1, 3, 4, 5] [2] ==> [1, 2, 3, 4, 5]

function mergeSort(array) {
  // base case
  if (array.length <= 1) return array;

  // split the array in half
  let middle = Math.floor(array.length / 2);
  let left = mergeSort(array.slice(0, middle));
  let right = mergeSort(array.slice(middle));

  console.log('left', left);
  console.log('right', right);

  // merge the arrays
  return merge(left, right);
}

function merge(array1, array2) {
  let result = [];
  let i = 0;
  let j = 0;

  // while there are elements in both arrays
  while (i < array1.length && j < array2.length) {
    // push the smaller element
    if (array1[i] < array2[j]) {
      result.push(array1[i]);
      i++;
    } else {
      result.push(array2[j]);
      j++;
    }
  }

  // while there are elements in array1
  while (i < array1.length) {
    result.push(array1[i]);
    i++;
  }

  // while there are elements in array2
  while (j < array2.length) {
    result.push(array2[j]);
    j++;
  }

  return result;
}

const numbers = [5, 3, 4, 1, 2];
console.log(mergeSort(numbers));

