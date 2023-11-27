// radix sort definition: A sorting algorithm where we sort numbers by their individual digits.
// example: [5, 3, 4, 1, 2] ==> [1, 2, 3, 4, 5]

function radixSort(array) {
  // find the max number and multiply it by 10 to get a number
  // with no. of digits of max + 1
  const maxNum = Math.max(...array) * 10;
  let divisor = 10;

  while (divisor < maxNum) {
    // create bucket arrays for each of 0-9
    let buckets = [...Array(10)].map(() => []);

    // put numbers into buckets based on their digit at divisor place
    for (let num of array) {
      buckets[Math.floor((num % divisor) / (divisor / 10))].push(num);
    }

    // put numbers back into array after flattening and emptying buckets
    array = [].concat.apply([], buckets);

    // move to the next significant digit
    divisor *= 10;
  }

  return array;
}

const numbers = [5, 3, 4, 1, 2];
console.log(radixSort(numbers));