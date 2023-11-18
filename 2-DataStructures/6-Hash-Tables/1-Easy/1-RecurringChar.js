// Given an array, return the first recurring character.
//
// Example:
// Given: [2,5,1,2,3,5,1,2,4]
// Return: 2
//
// Given: [2,1,1,2,3,5,1,2,4]
// Return: 1
//
// Given: [2,3,4,5]
// Return: undefined

// Solution 1: Brute Force
// Time Complexity: O(n^2)
// Space Complexity: O(1)
function firstRecurringCharacter(array) {
  for (let i = 0; i < array.length; i++) {
    let current = array[i];
    for (let j = i + 1; j < array.length; j++) {
      if (current === array[j]) {
        return current;
      }
    }
  }
  return undefined;
}

// Solution 2: Hash Table
// Time Complexity: O(n)
// Space Complexity: O(n)
function firstRecurringCharHashTable(array) {
  let map = {};
  for (let index = 0; index < array.length; index++) {
    const element = array[index];

    if (map[element]) {
      return element;
    }
     map[element] = index;
  }

  return undefined;
}

// Solution 3: Hash Table
// Time Complexity: O(n)
// Space Complexity: O(n)
function firstRecurringCharHashTable2(array) {
  let map = new Map();
  for (let index = 0; index < array.length; index++) {
    const element = array[index];

    if (map.has(element)) {
      return element;
    }
    map.set(element, index);
  }

  return undefined;
}

// testing
console.log(firstRecurringCharacter([2, 5, 1, 2, 3, 5, 1, 2, 4])); // 2
console.log(firstRecurringCharacter([2, 1, 1, 2, 3, 5, 1, 2, 4])); // 1
console.log(firstRecurringCharacter([2, 3, 4, 5])); // undefined
console.log(firstRecurringCharHashTable([2, 5, 1, 2, 3, 5, 1, 2, 4])); // 2
console.log(firstRecurringCharHashTable([2, 1, 1, 2, 3, 5, 1, 2, 4])); // 1
console.log(firstRecurringCharHashTable([2, 3, 4, 5])); // undefined
console.log(firstRecurringCharHashTable2([2, 5, 1, 2, 3, 5, 1, 2, 4])); // 2
console.log(firstRecurringCharHashTable2([2, 1, 1, 2, 3, 5, 1, 2, 4])); // 1
console.log(firstRecurringCharHashTable2([2, 3, 4, 5])); // undefined