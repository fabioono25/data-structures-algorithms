// example of a logaritmic time complexity O(log n)

// O(log n) - Logarithmic Time
// example: binary search

const binarySearch = (sortedArray, target) => {
  let left = 0;
  let right = sortedArray.length - 1;

  while (left <= right) {
      let mid = Math.floor((left + right) / 2);
      if (sortedArray[mid] === target) {
          return mid; // Element found at index mid
      } else if (sortedArray[mid] < target) {
          left = mid + 1;
      } else {
          right = mid - 1;
      }
  }

  return -1; // Element not found in the array
}

const binarySearch2 = (array, target) => {
  let startIndex = 0;
  let endIndex = array.length - 1;
  while (startIndex <= endIndex) {
    let middleIndex = Math.floor((startIndex + endIndex) / 2);
    if (target === array[middleIndex]) {
      return console.log("Target was found at index " + middleIndex);
    }
    if (target > array[middleIndex]) {
      console.log("Searching the right side of Array");
      startIndex = middleIndex + 1;
    }
    if (target < array[middleIndex]) {
      console.log("Searching the left side of array");
      endIndex = middleIndex - 1;
    } else {
      console.log("Not Found this loop iteration. Looping another iteration.");
    }
  }

  console.log("Target value not found in array");
}

const largestPowerOfTwo = (n) => {
  let power = 1;
  while (power * 2 <= n) {
      power *= 2;
  }
  return power;
}

const countDigits = (number) => {
  if (number === 0) {
      return 1; // 0 has 1 digit
  }
  // Logarithm base 10 gives the number of digits in the integer
  return Math.floor(Math.log10(number)) + 1;
}

console.log(binarySearch([1, 2, 3, 4, 5, 6], 5));
console.log(binarySearch2([1, 2, 3, 4, 5, 6], 5));
console.log(largestPowerOfTwo(5));
console.log(countDigits(1234));
