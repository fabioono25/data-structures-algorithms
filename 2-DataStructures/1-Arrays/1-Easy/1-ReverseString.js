// Given an array, I want to reverse it.
// Example: 'Hi, how are you?' should be: '?uoy era woh ,iH'

// Solution 1:
function reverseArray(arr) {
  const reversedArray = [];

  // add validations: consider if it is necessary or not

  for (let index = arr.length-1; index >= 0; index--) {
    reversedArray.push(arr[index]);
  }

  return reversedArray;
}

// Solution 2: using spread operator
function reverseArray2(arr) {
  return [...arr].reverse();
}

// solution 3: using spread operator
const reverseArray3 = (arr) => [...arr].reverse().join('');


const phrase = 'Hi, how are you?';
console.log('original phrase: ', phrase);
console.log('reversed phrase: ', reverseArray(phrase).join(''));
console.log('reversed phrase: ', reverseArray2(phrase).join(''));
console.log('reversed phrase: ', reverseArray3(phrase));
