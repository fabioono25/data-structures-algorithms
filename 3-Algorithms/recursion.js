// recursion definition: A process (a function in our case) that calls itself
// 1. Invoke the same function with a different input until you reach your base case
// 2. Base case: The condition when the recursion ends

// Example 1: Count down
function countDown(num) {
  if (num <= 0) {
    console.log("All done!");
    return;
  }
  console.log(num);
  num--;
  countDown(num);
}

// Factorial - Definition: A factorial is the product of an integer and all the integers below it
// Example: 4! = 4 * 3 * 2 * 1 = 24

// Factorial: no recursion
function factorial(num) {
  let total = 1;
  for (let i = num; i > 0; i--) {
    total *= i;
  }
  return total;
}

// Factorial: using recursion
function factorialRec(num) {
  if (num === 1) return 1;
  return num * factorialRec(num - 1);
}

// Fibonacci sequence - Definition: A series of numbers in which each number (Fibonacci number) is the sum of the two preceding numbers
// Example: 1, 1, 2, 3, 5, 8, 13, 21, 34, 55
// fib(4) = fib(3) + fib(2) = 2 + 1 = 3
// fib(0) = 0, fib(1) = 1, fib(2) = 1, fib(3) = 2, fib(4) = 3, fib(5) = 5, fib(6) = 8

// no recursion
function fibonacci(num) {
  let arr = [0,1];

  for (let i = 2; i < num + 1; i++) {
    arr.push(arr[i-2] + arr[i-1]);
  }

  return arr[num];
}

function fibonacciRec(num) {
  // O(2^n)
  if (num < 2) return num;
  return fibonacciRec(num - 1) + fibonacciRec(num - 2);
}

// reverse string without recursion and without built-in functions
function reverse(str) {
  let reversed = "";

  for (let i = str.length - 1; i >= 0; i--) {
    reversed += str[i];
  }

  return reversed;
}

// reverse string using recursion
function reverseRec(str) {
  if (str === "") return "";
  return reverseRec(str.substr(1)) + str.charAt(0);
}


console.log("Example 1: Count down", countDown(3));
console.log("Factorial: no recursion", factorial(5));
console.log("Factorial: using recursion", factorialRec(5));
console.log("Fibonacci: no recursion", fibonacci(6));
console.log("Fibonacci: using recursion", fibonacciRec(6));
console.log("Reverse string: no recursion", reverse("hello"));
console.log("Reverse string: using recursion", reverseRec("hello"));