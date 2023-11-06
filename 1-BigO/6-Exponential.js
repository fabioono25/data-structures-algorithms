// examples of a Exponential Time Complexity O(2^n)

// O(2^n) - Exponential Time Complexity

// Example 1
// O(2^n) + O(2^n) = O(2^n)
const example1 = (n) => {
  if (n <= 1) return;
  example1(n - 1);
  example1(n - 1);
};

// Example 2: receiving an array
// O(2^n) + O(2^n) = O(2^n)
const example2 = (arr) => {
  if (!arr.length) return;
  const first = arr.shift();
  example2(arr);
  example2(arr);
};

// subset generation
// O(2^n)
const subset = (arr) => {
  if (!arr.length) return [[]];
  const first = arr.shift();
  const subsets = subset(arr);
  const newSubsets = subsets.map((subset) => [first, ...subset]);
  return [...subsets, ...newSubsets];
};

// fibonacci
// O(2^n)
const fib = (n) => {
  if (n <= 2) return 1;
  return fib(n - 1) + fib(n - 2);
};

console.log("example1(3): ", example1(3));
console.log("example2([1, 2, 3]): ", example2([1, 2, 3]));
console.log("subset([1, 2, 3]): ", subset([1, 2, 3]));
console.log("fib(6): ", fib(6));