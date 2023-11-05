// example of a quadratic time complexity O(n^2)

// O(n^2) - Quadratic Time
// the number of operations is proportional to the square of the number of elements
// example: bubble sort

// example 1: nested for loops
const printAllPairs = (array) => {
  for (let i = 0; i < array.length; i++) { // n operations
    for (let j = 0; j < array.length; j++) { // n operations
      console.log(array[i], array[j]); // n * n operations
    }
  }
};

// example 2: bubble sort
const bubbleSort = (array) => {
  for (let i = 0; i < array.length; i++) { // n operations
    for (let j = 0; j < array.length; j++) { // n operations
      if (array[j] > array[j + 1]) { // n * n operations
        let temp = array[j]; // n * n operations
        array[j] = array[j + 1]; // n * n operations
        array[j + 1] = temp; // n * n operations
      }
    }
  }
  return array; // 1 operation
};

// example 3: string matching
const stringMatch = (str1, str2) => {
  let matches = "";
  for (let i = 0; i < str1.length; i++) { // n operations
    for (let j = 0; j < str2.length; j++) { // n operations
      if (str1[i] === str2[j]) { // n * n operations
        matches += str1[i]; // n * n operations
      }
    }
  }
  return matches; // 1 operation
};

// example 4: another example of nested for loops
const printAllPairs2 = (array) => {
  for (let i = 0; i < array.length; i++) { // n operations
    for (let j = 0; j < array.length; j++) { // n operations
      for (let k = 0; k < array.length; k++) { // n * n operations
        console.log(array[i], array[j], array[k]); // n * n * n operations
      }
    }
  }
};

// example 5: another example of O(n^2)
const printAllPairs3 = (array) => {
  for (let i = 0; i < array.length; i++) { // n operations
    for (let j = 0; j < array.length; j++) { // n operations
      console.log(array[i], array[j]); // n * n operations
    }
  }
  for (let k = 0; k < array.length; k++) { // n operations
    console.log(array[k]); // n operations
  }
};

console.log("Print All Pairs: ", printAllPairs([1, 2, 3, 4, 5, 6]));
console.log("Bubble Sort: ", bubbleSort([1, 2, 3, 4, 5, 6]));
console.log("String Match: ", stringMatch("hello", "world"));
console.log("Print All Pairs 2: ", printAllPairs2([1, 2, 3, 4, 5, 6]));
console.log("Print All Pairs 3: ", printAllPairs3([1, 2, 3, 4, 5, 6]));
