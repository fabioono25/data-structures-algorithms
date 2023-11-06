// examples of a Linearithmic Time Complexity O(n log n)

// O(n log n) - Linearithmic Time Complexity

// Example 1
// O(n) + O(n log n) = O(n log n)
const example1 = (n) => {
  for (let i = 0; i < n; i++) {
    console.log(i);
  }
  for (let j = 1; j <= n; j *= 2) {
    console.log(j);
  }
};

// Example 2
// O(n log n) + O(n log n) = O(n log n)
const example2 = (n) => {
  for (let i = 1; i <= n; i *= 2) {
    console.log(i);
  }
  for (let j = 1; j <= n; j *= 2) {
    console.log(j);
  }
};

// Example 3: mergeSort
// O(n log n)
const mergeSort = (arr) => {
  if (arr.length < 2) return arr;
  const middle = Math.floor(arr.length / 2);
  const leftArr = arr.slice(0, middle);
  const rightArr = arr.slice(middle);
  return merge(mergeSort(leftArr), mergeSort(rightArr));
};

// example 4: quickSort
const quickSort = (arr) => {
  if (arr.length < 2) return arr;
  const pivot = arr[0];
  const leftArr = [];
  const rightArr = [];
  for (let i = 1; i < arr.length; i++) {
    if (arr[i] < pivot) leftArr.push(arr[i]);
    else rightArr.push(arr[i]);
  }
  return quickSort(leftArr).concat(pivot, quickSort(rightArr));
}

// example 5: heapSort
const heapSort = (arr) => {
  const sorted = [];
  while (arr.length) {
    heapify(arr);
    sorted.unshift(arr.shift());
  }
  return sorted;
};

// example 6: BST - Time Complexity: O(n log n)
class Node {
  constructor(value) {
      this.value = value;
      this.left = null;
      this.right = null;
  }
}

class BinarySearchTree {
  constructor() {
      this.root = null;
  }

  // BST operations (insertion, searching, deletion) logic
}

const testBst = () => {
  const bst = new BinarySearchTree();
  bst.insert(9);
  bst.insert(4);
  bst.insert(6);
  bst.insert(20);
  bst.insert(170);
  bst.insert(15);
  bst.insert(1);
  console.log(bst);
  console.log(bst.lookup(9));
  console.log(bst.lookup(4));
  console.log(bst.lookup(6));
  console.log(bst.lookup(20));
  console.log(bst.lookup(170));
  console.log(bst.lookup(15));
  console.log(bst.lookup(1));
}

console.log('example1: ', example1(10));
console.log('example2: ', example2(10));
console.log('mergeSort: ', mergeSort([10, 24, 76, 73, 72, 1, 9]));
console.log('quickSort: ', quickSort([10, 24, 76, 73, 72, 1, 9]));
console.log('heapSort: ', heapSort([10, 24, 76, 73, 72, 1, 9]));
console.log('testBst: ', testBst());
