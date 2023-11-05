// example of a constant time complexity O(1)

// O(1) - Constant Time
// no matter how many elements we're working with, the algorithm/operation will always take the same amount of time
// example: looking up an element in an array by its index

const findFirst = (array) => array[0];

const findLast = (array) => array[array.length - 1];

const isEvenOrOdd = (number) => {
  if (number % 2 === 0) {
    return "Even";
  } else {
    return "Odd";
  }
};

const findNth = (array, n) => array[n - 1];

// O(1 + 1) -> O(2) -> O(1)
const firstAndLast = (array) => [array[0], array[array.length - 1]];

const getValueForKey = (key) => hashMap.get(key);

const swapVariables = (a, b) => {
  a = a + b;
  b = a - b;
  a = a - b;
  return [a, b];
};

const getElementAtIndex = (arr, index) => {
  if (index >= 0 && index < arr.length) {
    return arr[index];
  } else {
    return "Index out of bounds";
  }
};

const getValueForKey2 = (dict, key) => dict[key] || "Key not found";

console.log("First: ", findFirst([1, 2, 3, 4, 5, 6]));
console.log("Last: ", findLast([1, 2, 3, 4, 5, 6]));
console.log("Even or Odd: ", isEvenOrOdd(2));
console.log("Even or Odd: ", isEvenOrOdd(3));
console.log("Nth: ", findNth([1, 2, 3, 4, 5, 6], 3));
console.log("First and Last: ", firstAndLast([1, 2, 3, 4, 5, 6]));

const hashMap = new Map();
hashMap.set("key1", "value1");
hashMap.set("key2", "value2");
hashMap.set("key3", "value3");
console.log("Hash Map: ", getValueForKey("key1"));

console.log("Swap Variables: ", swapVariables(1, 2));
console.log("Get Element at Index: ", getElementAtIndex([1, 2, 3, 4, 5, 6], 3));

const dictionary = {
  key1: "value1",
  key2: "value2",
  key3: "value3",
};

console.log("Get Value for Key: ", getValueForKey2(dictionary, "key1"));
