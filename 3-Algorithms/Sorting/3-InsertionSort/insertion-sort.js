// Insertion Sort definition: A sorting algorithm where we gradually create a larger left half which is always sorted
// Example: [5, 3, 4, 1, 2] ==> [3, 5, 4, 1, 2] ==> [3, 4, 5, 1, 2] ==> [1, 3, 4, 5, 2] ==> [1, 2, 3, 4, 5]

// function selectionSort(array) {
//   for (i = 0; i < array.length; i++) {  
//     let minIndex = i;
//     let temp = array[i];

//     for (j = i + 1; j < array.length; j++) {
//       if (array[j] < array[minIndex]) {
//         // if the current is lower than the min, we have a new min
//         minIndex = j;
//       }
//     }

//     array[i] = array[minIndex];
//     array[minIndex] = temp;
//   }
// }

// // is there a way to improve the selection sort?
// // yes, we can add a variable to check if the array is already sorted
// // if it is, we can break the loop
// // we can also add a variable to check if we made any swaps
// // if we didn't, we can break the loop
// // example: 
// function selectionSortOptimized(array) {
//   for (i = 0; i < array.length; i++) {  
//     let minIndex = i;
//     let temp = array[i];
//     let noSwaps = true;

//     for (j = i + 1; j < array.length; j++) {
//       if (array[j] < array[minIndex]) {
//         // if the current is lower than the min, we have a new min
//         minIndex = j;
//         noSwaps = false;
//       }
//     }

//     if (noSwaps) break;

//     array[i] = array[minIndex];
//     array[minIndex] = temp;
//   }
// }

// const numbers = [5, 3, 4, 1, 2];
// selectionSort(numbers);
// console.log(numbers);

// const numbers2 = [5, 3, 4, 1, 2];
// selectionSortOptimized(numbers2);
// console.log(numbers2);
