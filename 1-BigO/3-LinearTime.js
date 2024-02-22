// examples of a linear time complexity O(n)

// O(n) - Linear Time
// the number of operations is directly proportional to the number of elements
// example: iterating over the elements in an array

const findMax = (array) => {
  let max = array[0]; // 1 operation
  for (let i = 1; i < array.length; i++) { // n operations
    if (array[i] > max) { // n - 1 operations
      max = array[i]; // n - 1 operations
    }
  }
  return max; // 1 operation
};

// searching for an element in an unsorted array
const linearSearch = (arr, target) => {
  for (let i = 0; i < arr.length; i++) {
      if (arr[i] === target) {
          return i;
      }
  }
  return -1; // Element not found
}

// fn: it prints the numbers from 0 to n
// fn is O(n) because it depends on the size of n
fn = (n) => {
  for (let i = 0; i < n; i++) {
    console.log(i);
  }
};

const sumElements = (arr) => {
  let sum = 0;
  for (let i = 0; i < arr.length; i++) {
      sum += arr[i];
  }
  return sum;
}

const countOccurrences = (arr, target) => {
  let count = 0;
  for (let i = 0; i < arr.length; i++) {
      if (arr[i] === target) {
          count++;
      }
  }
  return count;
}

console.log("Max: ", findMax([1, 2, 3, 4, 5, 6]));
console.log("Linear Search: ", linearSearch([1, 2, 3, 4, 5, 6], 3));
console.log("fn: ", fn(5));
console.log("Sum: ", sumElements([1, 2, 3, 4, 5, 6]));
console.log("Count: ", countOccurrences([1, 2, 3, 4, 5, 6], 3));