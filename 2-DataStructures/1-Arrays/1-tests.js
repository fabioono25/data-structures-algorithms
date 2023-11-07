// 4 items in a 32 bits system = 16 bytes of storage
const arr1 = [1, 'b', 'c', 3]

arr1.push('dd'); // O(1) - adding at the end of the array

arr1.pop(); // O(1) - removing at the end of the array
arr1.pop();

arr1.unshift('aa'); // O(n) - adding at the beginning of the array
arr1.unshift('bb');
arr1.shift(); // O(n) - removing at the beginning of the array

arr1.splice(2, 0, 'cc'); // O(n) - inserting at a specific index

console.log('arr1: ', arr1);
console.log('arr1[2]: ', arr1[2]); // O(1) - accessing an element by index

// JS, Python (lists), Java (ArrayLists) - Dynamic Arrays
// C, C++ - Static Arrays
// Dynamic arrays expand as you add more elements
// Static arrays have a fixed size
