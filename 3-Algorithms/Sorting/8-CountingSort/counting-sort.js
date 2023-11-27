// counting sort definition: A sorting algorithm where we create a bucket for each value and keep a counter in each bucket. Then, we add values back to the original array based on the number of times they appear in the bucket.
// example: [5, 3, 4, 1, 2] ==> [1, 2, 3, 4, 5]

function countingSort(array) {
  // find max value in array
  let max = Math.max(...array);
  // create an array with the length of max + 1 and fill it with 0
  let countArray = new Array(max + 1).fill(0);
  // create an array to store the sorted values
  let sortedArray = [];

  // loop through array and add 1 to the index of countArray
  // that corresponds to the value of the current element
  for (let i = 0; i < array.length; i++) {
    countArray[array[i]]++;
  }

  // loop through countArray
  for (let i = 0; i < countArray.length; i++) {
    // loop through countArray at the current index
    for (let j = 0; j < countArray[i]; j++) {
      // push the index to sortedArray
      sortedArray.push(i);
    }
  }

  return sortedArray;
}

const numbers = [5, 3, 4, 1, 2];
console.log(countingSort(numbers));