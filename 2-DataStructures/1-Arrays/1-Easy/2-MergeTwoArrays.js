// Given two sorted arrays, merge them into one array.
// Example: [1, 2, 3] and [4, 5, 6, 8, 10] should be [1, 2, 3, 4, 5, 6, 8, 10]

const mergeTwoArrays = (arr1, arr2) => {
  const mergedArray = [];

  if (arr1.length === 0) {
    return arr2;
  }

  if (arr2.length === 0) {
    return arr1;
  }

  // O(n) - linear time
  for (let index = 0; index < arr1.length; index++) {
    mergedArray.push(arr1[index]);
  }

  // O(n) - linear time
  for (let index = 0; index < arr2.length; index++) {
    mergedArray.push(arr2[index]);
  }

  return mergedArray;
} // O(n) + O(n) = O(2n) = O(n)

// using while loop
const mergeTwoArrays2 = (arr1, arr2) => {

  const mergedArray = [];
  let index1 = 0;
  let index2 = 0;

  while (index1 < arr1.length || index2 < arr2.length) {
    if (arr1[index1] < arr2[index2]) {
      mergedArray.push(arr1[index1]);
      index1++;
    } else {
      mergedArray.push(arr2[index2]);
      index2++;
    }
  }

  return mergedArray;


}

// O(n) - linear time
const mergeTwoArrays3 = (arr1, arr2) => {
  return [...arr1, ...arr2];
}

const arr1 = [1, 2, 3];
const arr2 = [4, 5, 6, 8, 10];
console.log('arr1: ', arr1);
console.log('arr2: ', arr2);
console.log('merged array: ', mergeTwoArrays(arr1, arr2));
console.log('merged array: ', mergeTwoArrays2(arr1, arr2));
console.log('merged array: ', mergeTwoArrays3(arr1, arr2));