# Data Structures and Algorithms - JavaScript

## Table of Contents

- [Data Structures and Algorithms - JavaScript](#data-structures-and-algorithms---javascript)
  - [Table of Contents](#table-of-contents)
  - [Big-O Notation](#big-o-notation)
    - [Time Complexity](#time-complexity)
      - [O(1) Constant Time Complexity](#o1-constant-time-complexity)
        - [Definition](#definition)
        - [Advantages](#advantages)
        - [Disadvantages](#disadvantages)
        - [Use-Cases](#use-cases)
      - [O(n) Linear Time Complexity](#on-linear-time-complexity)
        - [Definition](#definition-1)
        - [Advantages](#advantages-1)
        - [Disadvantages](#disadvantages-1)
        - [Use-Cases](#use-cases-1)
      - [O(n^2) Quadratic Time Complexity](#on2-quadratic-time-complexity)
        - [Definition](#definition-2)
        - [Advantages](#advantages-2)
        - [Disadvantages](#disadvantages-2)
        - [Use-Cases](#use-cases-2)
      - [O(log n) Logaritmic Time Complexity](#olog-n-logaritmic-time-complexity)
        - [Definition](#definition-3)
        - [Advantages](#advantages-3)
        - [Disadvantages](#disadvantages-3)
        - [Use-Cases](#use-cases-3)
      - [O(n log n) Linearithmic Time Complexity](#on-log-n-linearithmic-time-complexity)
        - [Definition](#definition-4)
        - [Advantages](#advantages-4)
        - [Disadvantages](#disadvantages-4)
        - [Use-Cases](#use-cases-4)
      - [O(2^n) Exponential Time Complexity](#o2n-exponential-time-complexity)
        - [Definition](#definition-5)
        - [Advantages](#advantages-5)
        - [Disadvantages](#disadvantages-5)
        - [Use-Cases](#use-cases-5)
      - [O(n!) Factorial Time Complexity](#on-factorial-time-complexity)
        - [Definition](#definition-6)
        - [Advantages](#advantages-6)
        - [Disadvantages](#disadvantages-6)
        - [Use-Cases](#use-cases-6)
    - [Space Complexity](#space-complexity)
  - [The Four Rules in Big-O](#the-four-rules-in-big-o)
  - [Data Structures](#data-structures)
    - [Arrays](#arrays)
      - [Definition](#definition-7)
      - [Advantages](#advantages-7)
      - [Disadvantages](#disadvantages-7)
      - [Use-Cases](#use-cases-7)
    - [Singly Linked Lists](#singly-linked-lists)
      - [Definition](#definition-8)
      - [Advantages](#advantages-8)
      - [Disadvantages](#disadvantages-8)
      - [Use-Cases](#use-cases-8)
    - [Doubly-Linked Lists](#doubly-linked-lists)
      - [Definition](#definition-9)
      - [Advantages](#advantages-9)
      - [Disadvantages:](#disadvantages-9)
      - [Use-Cases](#use-cases-9)
    - [Stacks](#stacks)
      - [Definition](#definition-10)
      - [Advantages](#advantages-10)
      - [Disadvantages](#disadvantages-10)
      - [Use-Cases](#use-cases-10)
    - [Queues](#queues)
      - [Definition](#definition-11)
      - [Advantages](#advantages-11)
      - [Disadvantages](#disadvantages-11)
      - [Use-Cases](#use-cases-11)
    - [Hash Tables](#hash-tables)
      - [Definition](#definition-12)
      - [Advantages](#advantages-12)
      - [Disadvantages](#disadvantages-12)
      - [Use-Cases](#use-cases-12)
    - [Trees](#trees)
      - [Definition](#definition-13)
      - [Advantages](#advantages-13)
      - [Disadvantages](#disadvantages-13)
      - [Use-Cases](#use-cases-13)
    - [Graphs](#graphs)
      - [Definition](#definition-14)
    - [**Advantages:**](#advantages-14)
    - [**Disadvantages:**](#disadvantages-14)
      - [Use-Cases](#use-cases-14)
  - [Recursion](#recursion)
    - [**Advantages**](#advantages-15)
    - [**Disadvantages**](#disadvantages-15)
  - [Sorting Algorithms](#sorting-algorithms)
    - [Bubble Sort](#bubble-sort)
    - [Selection Sort](#selection-sort)
    - [Insertion Sort](#insertion-sort)
      - [Definition](#definition-15)
    - [Merge Sort](#merge-sort)
      - [Definition](#definition-16)
    - [Quick Sort](#quick-sort)
      - [Definition](#definition-17)
    - [Heap Sort](#heap-sort)
      - [Definition](#definition-18)
    - [Radix Sort](#radix-sort)
      - [Definition](#definition-19)
  - [Searching Algorithms](#searching-algorithms)
    - [Linear Search](#linear-search)
      - [Definition](#definition-20)
    - [Binary Search](#binary-search)
      - [Definition](#definition-21)
    - [Breadth-First Search (BFS)](#breadth-first-search-bfs)
      - [Definition](#definition-22)
    - [Depth-First Search (DFS)](#depth-first-search-dfs)
      - [Definition](#definition-23)
  - [Links](#links)

## Big-O Notation

Big O notation is a mathematical notation that describes the limiting behavior of a function when the argument approaches infinity. In computer science, it is used to express the upper bound or worst-case time complexity of an algorithm in terms of the size of its input. It provides a simplified representation of how the runtime or space requirements of an algorithm grow as the input size increases.

![Big-O Complexity Chart](assets/20231105_122936_bigO.png "Big-O Complexity Chart")
Source: [Big-O Cheat Sheet](https://www.bigocheatsheet.com/)

### Time Complexity

Time Complexity measures the amount of time an algorithm takes to run as a function of the input size. Focused on how the execution time increases, given the input size.

---

#### O(1) Constant Time Complexity

##### Definition

Algorithms with constant time complexity always take the same amount of time to execute, regardless of the size of the input. These algorithms have a fixed and predictable runtime.

##### Advantages

* **Predictable Performance:** Algorithms with constant time complexity always have the same execution time, making them **predictable** and **reliable**, regardless of input size.
* **Efficiency for Small Inputs:** Constant time complexity algorithms are ideal for operations where the input size is always a fixed number or very small, ensuring **fast execution**.
* **Optimal for Real-Time Systems:** In **real-time applications**, constant time complexity ensures that operations are completed within a fixed time frame, essential for time-sensitive tasks.

##### Disadvantages

* **Limited Applicability:** Constant time complexity algorithms are limited to specific operations and scenarios where the input size does not affect the algorithm's performance.
* **Not Suitable for Complex Problems:** Algorithms with constant time complexity cannot handle complex computational tasks or problems that require processing large datasets.
* **Difficult to Achieve:** Designing algorithms with constant time complexity is challenging and often not achievable for many real-world problems.

##### Use-Cases

**Accessing Elements in an Array or List:**

Retrieving an element from an array or list using its index. Regardless of the size of the array, accessing elements by index takes constant time because the index directly points to the memory location of the element.

```javascript
function getElementAtIndex(arr, index) {
    return arr[index];
}
```

**Checking Hash Table (HashMap) for Key-Value Pairs:**

Accessing values in a hash table (or hashmap) based on a known key. Hash tables use a hashing function to directly map keys to their corresponding values, allowing for constant time complexity for retrieval operations.

```javascript
const hashMap = {
    "key1": "value1",
    "key2": "value2",
    // ...
};

function getValueForKey(key) {
    return hashMap[key] || "Key not found";
}
```

**Operations on Fixed-Size Data Structures:**

Operations on data structures with a fixed size, such as a fixed-size array, involve constant time complexity. For example, swapping values between two variables without using additional storage takes constant time.

```javascript
function swapVariables(a, b) {
    a = a + b;
    b = a - b;
    a = a - b;
    return [a, b];
}
```

In these scenarios, the time taken for the operations remains constant regardless of the size of the input data, making algorithms with O(1) constant time complexity ideal for these use-cases.

---

#### O(n) Linear Time Complexity

##### Definition

Linear time complexity algorithms have a runtime proportional to the input size, making them suitable for small to moderate-sized datasets.

##### Advantages

* **Simplicity:** Linear time complexity algorithms are often simple to implement and understand, making them accessible for a wide range of developers.
* **Scalability:** Linear time complexity algorithms can handle larger datasets efficiently, making them suitable for moderate-sized inputs.
* **Straightforward Iteration:** Algorithms with linear time complexity often involve straightforward iterations through data structures, making them applicable to various tasks.

##### Disadvantages

* **Limited Scalability:** Linear time complexity algorithms become slow for very large datasets, as their execution time increases linearly with input size.
* **Inefficient for Complex Operations:** Algorithms with linear time complexity may not be efficient for complex computations or tasks requiring intricate data manipulations.
* **Not Suitable for Real-Time Systems:** In real-time applications where quick responses are crucial, linear time complexity algorithms might not provide the necessary speed.

##### Use-Cases

**Linear Search:**

Linear search is a straightforward algorithm for finding a target element in an unsorted list or array. It compares each element in the list with the target value until a match is found or the entire list is
traversed. Linear search has O(n) time complexity because, in the worst case, it may need to check every element in the list.

```javascript
const linearSearch = (arr, target) => {
    for (let i = 0; i < arr.length; i++) {
        if (arr[i] === target) {
            return i; // Element found at index i
        }
    }
    return -1; // Element not found in the list
}
```

**Calculating Sum of Elements:**

Calculating the sum of elements in a list or array involves iterating through each element and adding it to a total sum. As the number of elements in the input increases, the number of iterations required also
increases linearly, resulting in O(n) time complexity.

```javascript
const calculateSum(arr) => {
    let sum = 0;
    for (let num of arr) {
        sum += num;
    }
    return sum;
}
```

**Filtering Elements Based on a Condition:**

Filtering elements that meet a specific condition from a list requires iterating through the entire list. For every element, the condition is checked, and if it's met, the element is included in the output. The
time complexity is O(n) as every element in the list might need to be examined.

```javascript
const filterNumbersGreaterThan(arr, threshold) => {
    let result = [];
    for (let num of arr) {
        if (num > threshold) {
            result.push(num);
        }
    }
    return result;
}
```

In these use-cases, the algorithms' runtime grows linearly with the size of the input data, making them suitable for tasks where the number of operations scales directly with the number of elements in the input.

---

#### O(n^2) Quadratic Time Complexity

##### Definition

Algorithms with quadratic time complexity have a runtime that is proportional to the square of the input size. Nested loops iterating over the input elements are a common cause of quadratic complexity. Performance deteriorates quickly for larger inputs.

##### Advantages

* **Simplicity and Readability:**
  Quadratic algorithms are often simpler to implement and easier to understand. The straightforward nature of nested loops and simple logic can make the code more readable, which is advantageous, especially for educational purposes or in scenarios where code clarity is crucial.
* **Suitable for Small Inputs:**
  Quadratic time complexity algorithms can be suitable for small input sizes. When dealing with small datasets, the performance difference between quadratic and more efficient algorithms might not be noticeable. In such cases, choosing a simpler quadratic algorithm can save development time and effort.
* **Lack of Complexity Scaling:**
  Quadratic time complexity algorithms may not significantly impact performance when the input size is small and fixed. In situations where the input size remains constant or is limited, the performance difference between quadratic and more efficient algorithms might not be a significant concern.

##### Disadvantages

* **Inefficiency for Large Inputs:**
  Quadratic algorithms become highly inefficient as the input size increases. Their execution time grows quadratically with the input size, leading to drastically longer processing times for larger datasets. This inefficiency can make them unsuitable for real-world applications dealing with substantial amounts of data.
* **Poor Scalability:**
  Quadratic time complexity algorithms do not scale well. Even a slight increase in the input size can lead to a significant increase in the number of operations performed. As a result, these algorithms might quickly become impractical for tasks involving moderate to large-sized datasets, impacting user experience and system performance.
* **Limited Applicability:**
  Quadratic time complexity algorithms are not suitable for many real-world applications and scenarios. Tasks involving extensive data processing, searching, sorting, or complex computations typically require more efficient algorithms. Choosing quadratic algorithms in such cases can lead to suboptimal performance and may not meet the required performance standards.

##### Use-Cases

**Bubble Sort:**
Bubble Sort is a simple sorting algorithm that repeatedly steps through the list, compares adjacent elements, and swaps them if they are in the wrong order. The algorithm's time complexity is O(n^2) in the worst-case scenario, making it inefficient for large datasets. However, it can be used for educational purposes or for sorting small datasets where simplicity is preferred over efficiency.

```javascript
function bubbleSort(arr) {
    const n = arr.length;
    for (let i = 0; i < n - 1; i++) {
        for (let j = 0; j < n - i - 1; j++) {
            if (arr[j] > arr[j + 1]) {
                // Swap elements if they are in the wrong order
                [arr[j], arr[j + 1]] = [arr[j + 1], arr[j]];
            }
        }
    }
    return arr;
}
```

**Brute-Force String Matching:**
Brute-force string matching compares each character of a pattern string against each character of a text string, sliding the pattern one position at a time. This results in a quadratic time complexity (O(n^2)), making it inefficient for large texts and patterns. Brute-force matching is used when more efficient algorithms like Knuth-Morris-Pratt or Boyer-Moore are not applicable or necessary.

```javascript
function bruteForceStringMatch(text, pattern) {
    const n = text.length;
    const m = pattern.length;
    const occurrences = [];

    for (let i = 0; i <= n - m; i++) {
        let j;
        for (j = 0; j < m; j++) {
            if (text[i + j] !== pattern[j]) {
                // Character mismatch, break the inner loop
                break;
            }
        }

        if (j === m) {
            // Pattern found, add the starting index to occurrences
            occurrences.push(i);
        }
    }

    return occurrences;
}
```

**Generating Permutations:**
Generating permutations of a set involves creating all possible arrangements of the elements. One way to generate permutations is using recursive backtracking, which results in a time complexity of O(n^2) for n elements. While not the most efficient method for large sets, it's a simple approach to generate permutations for smaller sets.

```javascript
function generatePermutations(arr) {
    const permutations = [];

    function backtrack(start) {
        if (start === arr.length) {
            permutations.push([...arr]);
            return;
        }

        for (let i = start; i < arr.length; i++) {
            // Swap elements to create permutations
            [arr[start], arr[i]] = [arr[i], arr[start]];
            backtrack(start + 1);
            // Undo the swap for backtracking
            [arr[start], arr[i]] = [arr[i], arr[start]];
        }
    }

    backtrack(0);
    return permutations;
}
```

> These use-cases highlight scenarios where algorithms with quadratic time complexity can be applied, either for educational purposes, small datasets, or when more efficient algorithms are not required or available.

---

#### O(log n) Logaritmic Time Complexity

##### Definition

Logarithmic time complexity algorithms reduce the size of the problem in each step by a logarithmic factor. These algorithms are often found in divide and conquer strategies, and they efficiently handle large
datasets by repeatedly dividing the problem space.

##### Advantages

* **Efficiency with Large Datasets:**
  Algorithms with O(log n) time complexity are highly efficient, especially when dealing with large datasets. They scale well and can handle significant amounts of data without a significant increase in execution time. This efficiency is valuable in applications dealing with extensive data processing.
* **Efficient Searching:**
  O(log n) time complexity is commonly associated with binary search algorithms. Searching in sorted data structures (such as sorted arrays or balanced binary search trees) using binary search significantly reduces the search space in each step. This efficiency makes binary search suitable for quick retrieval of specific elements from large datasets.
* **Balanced Tree Structures:**
  O(log n) time complexity is achievable for operations like insertion, deletion, and search in balanced tree structures, such as AVL trees and Red-Black trees. These tree structures maintain balance during operations, ensuring that the height of the tree remains logarithmic, leading to efficient operations even as the dataset grows.

##### Disadvantages

* **Complexity in Implementation:**
  Implementing algorithms with O(log n) time complexity, especially those involving complex data structures like balanced trees, can be challenging. Properly maintaining the balance and ensuring logarithmic height requires careful implementation, which can lead to more complex code.
* **Limited Applicability:**
  O(log n) time complexity is not always achievable for all types of operations or data structures. It's applicable mainly to tasks like searching in sorted data structures or efficient divide and conquer algorithms. For certain tasks, finding or designing algorithms with logarithmic time complexity might not be possible.
* **Memory Overhead:**
  Some data structures that achieve O(log n) time complexity, such as balanced trees, often require additional memory to maintain their balanced structure. This memory overhead can be a disadvantage, especially in memory-constrained environments. Additionally, the overhead associated with recursive function calls in certain logarithmic algorithms can impact memory usage.

##### Use-Cases

**Binary Search:**

Binary search is a classic example of an O(log n) algorithm. It efficiently finds the position of a target element in a sorted array by repeatedly dividing the search space in half.

```javascript
function binarySearch(sortedArray, target) {
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

// Example usage
const sortedArray = [1, 3, 5, 7, 9, 11, 13, 15];
const target = 7;
const resultIndex = binarySearch(sortedArray, target);
console.log(`Index of ${target} in the array: ${resultIndex}`);
```

**Finding Nth Fibonacci Number:**

Computing the nth Fibonacci number efficiently using matrix exponentiation techniques can achieve O(log n) time complexity.

```javascript
function matrixMultiply(matrix1, matrix2) {
    // Matrix multiplication logic
}

function power(matrix, n) {
    // Matrix exponentiation logic
}

function nthFibonacci(n) {
    const baseMatrix = [[1, 1], [1, 0]];
    const resultMatrix = power(baseMatrix, n - 1);
    return resultMatrix[0][0];
}

// Example usage
const n = 5;
const fibonacciNumber = nthFibonacci(n);
console.log(`The ${n}th Fibonacci number is: ${fibonacciNumber}`);
```

**Efficient Exponentiation:**

Calculating exponentiation efficiently using the divide and conquer method can achieve O(log n) time complexity.

```javascript
function power(base, exponent) {
    if (exponent === 0) {
        return 1;
    }
    const halfPower = power(base, Math.floor(exponent / 2));
    if (exponent % 2 === 0) {
        return halfPower * halfPower;
    } else {
        return base * halfPower * halfPower;
    }
}

// Example usage
const base = 2;
const exponent = 5;
const result = power(base, exponent);
console.log(`${base} raised to the power of ${exponent} is: ${result}`);
```

---

#### O(n log n) Linearithmic Time Complexity

##### Definition

Algorithms with linearithmic time complexity have an execution time that grows in proportion to n log ⁡n, where n**n** is the size of the input data. Many efficient sorting and searching algorithms, such as merge sort and heap sort, fall into this category.

##### Advantages

* **Efficient Sorting:**
  Algorithms with O(n log n) time complexity are often associated with **efficient sorting algorithms** like Merge Sort, Heap Sort, and QuickSort. These sorting algorithms are widely used due to their balanced performance, making them suitable for sorting large datasets efficiently.
* **Divide and Conquer Strategies:**
  Many divide and conquer algorithms achieve O(n log n) time complexity. These algorithms divide the problem into smaller subproblems, solve them independently, and then combine the solutions. This divide and conquer strategy allows for efficient processing of large datasets and is applicable to various computational problems.
* **Balanced Performance:**
  O(n log n) algorithms offer a balanced performance across a wide range of input sizes. While they are not as fast as linear algorithms (O(n)) for small datasets or constant time algorithms (O(1)) for specific operations, they provide efficient and manageable execution times for moderate to large datasets, making them versatile for various applications.

##### Disadvantages

* **Not Always Optimal:**
  O(n log n) time complexity is not always the optimal solution for all problems. For specific tasks with known input sizes or constraints, using algorithms with O(n) or even O(n^2) time complexity might be more efficient. Using O(n log n) algorithms when simpler solutions exist can result in unnecessary complexity.
* **Slower than Linear Time Algorithms for Small Inputs:**
  For small input sizes, algorithms with O(n log n) time complexity are slower than linear time algorithms (O(n)). The overhead of the divide and conquer strategy, as well as the additional comparisons and operations involved, can make O(n log n) algorithms less efficient than simpler linear algorithms when the input size is limited.
* **Higher Constant Factors:**
  O(n log n) algorithms often have higher constant factors in their execution times compared to simpler linear algorithms. This means that, even though they have a better overall growth rate than O(n^2) algorithms, they might be slower in practice for small to moderately sized datasets due to these overheads.

##### Use-Cases

**Sorting Large Datasets:**

O(n log n) sorting algorithms like Merge Sort, Heap Sort, and QuickSort are efficient for sorting large datasets. These algorithms guarantee a worst-case time complexity of O(n log n) and are widely used in various applications, such as organizing large databases, sorting files, and managing data in web applications.

```javascript
function mergeSort(arr) {
    if (arr.length <= 1) {
        return arr;
    }

    const mid = Math.floor(arr.length / 2);
    const left = mergeSort(arr.slice(0, mid));
    const right = mergeSort(arr.slice(mid));
    return merge(left, right);
}

function merge(left, right) {
    // Merge two sorted arrays logic
}

// Example usage
const unsortedArray = [5, 2, 9, 1, 5, 6];
const sortedArray = mergeSort(unsortedArray);
console.log("Sorted Array:", sortedArray);
```

**Efficient Searching in Large Datasets:**

Algorithms like Binary Search Trees (BST) or Balanced Binary Search Trees (e.g., AVL trees) maintain a sorted order, allowing efficient searching, insertion, and deletion operations in O(n log n) time complexity. These data structures are commonly used in dictionaries, databases, and various applications requiring quick search operations.

```javascript
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

// Example usage
const bst = new BinarySearchTree();
bst.insert(5);
bst.insert(2);
bst.insert(8);
bst.insert(1);
bst.insert(3);
const found = bst.search(3);
console.log("Element 3 found:", found);
```

**Merging Multiple Sorted Lists:**

Merging multiple sorted lists efficiently can be done in O(n log k) time complexity, where k is the number of lists. This operation is useful in various applications, such as merging results from multiple search engines, combining sorted arrays from different sources, or merging sorted data from distributed systems.

```javascript
function mergeKSortedLists(lists) {
    // Merge K sorted lists logic
}

// Example usage
const sortedLists = [[1, 4, 5], [1, 3, 6], [2, 7, 8]];
const mergedList = mergeKSortedLists(sortedLists);
console.log("Merged Sorted List:", mergedList);
```

---

#### O(2^n) Exponential Time Complexity

##### Definition

Exponential time complexity algorithms have an execution time that grows exponentially with the size of the input data. These algorithms become extremely slow as the input size increases, making them impractical for most real-world applications. Recursive algorithms with branching factors fall into this category.

##### Advantages

* **Simplicity and Readability:**
  Exponential time algorithms are often simpler and easier to understand due to their straightforward recursive nature. This simplicity can make the code more readable and maintainable, especially for educational purposes or when solving small-scale problems where efficiency is not a primary concern.
* **Guaranteed Solution:**
  Exponential algorithms explore all possible combinations or subsets of a given input. This exhaustive search ensures that the algorithm finds the correct solution (if one exists) without missing any possibilities. In some cases, this exhaustive approach is necessary to guarantee correctness.
* **Useful for Small Inputs:**
  Exponential algorithms can be practical for problems with small input sizes. When the input size is limited and within reasonable bounds, exponential algorithms can provide acceptable solutions, especially if other more efficient algorithms are not available or the problem is inherently complex.

##### Disadvantages

* **Exponential Growth:**
  The execution time of exponential algorithms grows exponentially with the input size. Even a slight increase in the input size can lead to a drastic increase in the number of operations performed. This exponential growth quickly makes these algorithms impractical for larger inputs.
* **Impractical for Moderate to Large Inputs:**
  Exponential algorithms become impractical for moderate to large input sizes. As the input size increases, the number of possible combinations or subsets grows exponentially, leading to extremely long computation times. These algorithms are not suitable for real-world applications with significant amounts of data.
* **High Time Complexity Classes:**
  Exponential time complexity (O(2^n)) falls into the category of high time complexity classes. Problems belonging to such classes are considered intractable and are generally not solvable in a reasonable amount of time for large inputs. Many problems in this class are classified as NP-hard, indicating their inherent complexity.

##### Use-Cases

**Subset Generation:**

Enumerating all subsets of a given set is a classic example where an exponential time algorithm can be applied. The number of subsets of a set with n elements is 2^n. Exponential time algorithms are used to generate all possible subsets, which find applications in combinatorial problems, power set generation, and various mathematical calculations.

```javascript
function generateSubsets(set) {
    const subsets = [];
    const n = set.length;
    for (let i = 0; i < (1 << n); i++) {
        const subset = [];
        for (let j = 0; j < n; j++) {
            if (i & (1 << j)) {
                subset.push(set[j]);
            }
        }
        subsets.push(subset);
    }
    return subsets;
}

// Example usage
const inputSet = [1, 2, 3];
const allSubsets = generateSubsets(inputSet);
console.log("All Subsets:", allSubsets);

```

**Traveling Salesman Problem (TSP):**

The Traveling Salesman Problem involves finding the shortest possible route that visits a set of cities and returns to the original city. The brute-force approach to solve TSP checks all permutations of the cities, leading to an exponential time complexity. Despite its inefficiency for large datasets, this approach guarantees an optimal solution.

```javascript
function calculateTotalDistance(path, graph) {
    // Calculate total distance for the given path using graph information
}

function generateAllPermutations(cities) {
    // Generate all permutations of cities
}

function bruteForceTSP(cities, graph) {
    const permutations = generateAllPermutations(cities);
    let minDistance = Infinity;
    let optimalPath = [];

    for (const permutation of permutations) {
        const distance = calculateTotalDistance(permutation, graph);
        if (distance < minDistance) {
            minDistance = distance;
            optimalPath = permutation;
        }
    }

    return { path: optimalPath, distance: minDistance };
}

// Example usage
const cities = [1, 2, 3];
const graph = {
    1: { 2: 10, 3: 15 },
    2: { 1: 10, 3: 20 },
    3: { 1: 15, 2: 20 }
};
const result = bruteForceTSP(cities, graph);
console.log("Optimal TSP Path:", result.path);
console.log("Total Distance:", result.distance);

```

**Subset Sum Problem:**

The Subset Sum Problem involves finding a subset of a given set of positive integers that adds up to a specific target sum. The brute-force approach generates all possible subsets and checks if any subset sums up to the target value. This exhaustive search leads to an exponential time complexity but guarantees finding a valid subset if one exists.

```javascript
function calculateTotalDistance(path, graph) {
    // Calculate total distance for the given path using graph information
}

function generateAllPermutations(cities) {
    // Generate all permutations of cities
}

function bruteForceTSP(cities, graph) {
    const permutations = generateAllPermutations(cities);
    let minDistance = Infinity;
    let optimalPath = [];

    for (const permutation of permutations) {
        const distance = calculateTotalDistance(permutation, graph);
        if (distance < minDistance) {
            minDistance = distance;
            optimalPath = permutation;
        }
    }

    return { path: optimalPath, distance: minDistance };
}

// Example usage
const cities = [1, 2, 3];
const graph = {
    1: { 2: 10, 3: 15 },
    2: { 1: 10, 3: 20 },
    3: { 1: 15, 2: 20 }
};
const result = bruteForceTSP(cities, graph);
console.log("Optimal TSP Path:", result.path);
console.log("Total Distance:", result.distance);

```

---

#### O(n!) Factorial Time Complexity

##### Definition

Factorial time complexity represents algorithms whose execution time grows factorially with the size of the input data. These algorithms are extremely slow and become practically unusable for even small input sizes. Examples include brute-force algorithms generating permutations or combinations.

##### Advantages

* **Guaranteed Optimal Solution:**
  Algorithms with factorial time complexity explore all possible permutations or combinations of a given set. This exhaustive search guarantees finding the optimal solution if one exists. In many combinatorial problems, the optimal solution can be discovered by examining all permutations or combinations.
* **Simplicity and Correctness:**
  Factorial time algorithms are often simple to implement, especially for smaller inputs, as they involve iterating through all possible permutations. Additionally, due to their exhaustive nature, they ensure correctness. These algorithms are straightforward to understand and can be used as brute-force methods for small-scale problems.
* **Useful for Small Input Sizes:**
  Factorial time algorithms can be practical for problems with very small input sizes. When the input size is limited and within reasonable bounds, using factorial time algorithms might be acceptable, especially if the problem's complexity demands an exhaustive search for a complete solution.

##### Disadvantages

* **Exponential Growth of Execution Time:**
  Factorial time complexity (O(n!)) leads to an explosion in the number of operations required as the input size increases. Even for moderately small inputs, the number of permutations becomes prohibitively large. As a result, the execution time grows at an astronomical rate, making these algorithms impractical for larger inputs.
* **Impractical for Moderate to Large Inputs:**
  Factorial time algorithms become impractical for moderate to large input sizes. The time required to compute all permutations increases factorially, making these algorithms inefficient and slow. They quickly become unusable as the input size grows, even for relatively simple problems.
* **Inefficiency and Limited Applicability:**
  Factorial time algorithms are generally inefficient for most real-world applications. Their inefficiency restricts their applicability to small-scale problems, and they are rarely used in production systems due to their impractical execution times. More efficient algorithms are usually preferred for solving practical problems.

##### Use-Cases

**Generating Permutations:**

Calculating all permutations of a given set is a classic use-case for O(n!) algorithms. Although inefficient, generating permutations can be useful in certain mathematical and combinatorial problems.

```javascript
function generatePermutations(inputArray) {
    if (inputArray.length <= 1) return [inputArray];
    const permutations = [];
    for (let i = 0; i < inputArray.length; i++) {
        const remainingArray = inputArray.slice(0, i).concat(inputArray.slice(i + 1));
        const partialPermutations = generatePermutations(remainingArray);
        for (const permutation of partialPermutations) {
            permutations.push([inputArray[i], ...permutation]);
        }
    }
    return permutations;
}

// Example usage
const inputArray = [1, 2, 3];
const allPermutations = generatePermutations(inputArray);
console.log("All Permutations:", allPermutations);

```

**Brute-Force Algorithm for Traveling Salesman Problem (TSP):**

A naive approach to solving the Traveling Salesman Problem (TSP) involves checking all permutations of cities to find the shortest route. Although impractical for large datasets, this brute-force method guarantees finding the optimal solution.

```javascript
function calculateTotalDistance(path, graph) {
    // Calculate total distance for the given path using graph information
}

function generateAllPermutations(cities) {
    // Generate all permutations of cities
}

function bruteForceTSP(cities, graph) {
    const permutations = generateAllPermutations(cities);
    let minDistance = Infinity;
    let optimalPath = [];

    for (const permutation of permutations) {
        const distance = calculateTotalDistance(permutation, graph);
        if (distance < minDistance) {
            minDistance = distance;
            optimalPath = permutation;
        }
    }

    return { path: optimalPath, distance: minDistance };
}

// Example usage
const cities = [1, 2, 3];
const graph = {
    1: { 2: 10, 3: 15 },
    2: { 1: 10, 3: 20 },
    3: { 1: 15, 2: 20 }
};
const result = bruteForceTSP(cities, graph);
console.log("Optimal TSP Path:", result.path);
console.log("Total Distance:", result.distance);

```

**Brute-Force Algorithm for Subset Sum Problem:**

The Subset Sum Problem involves finding a subset of a given set of positive integers that adds up to a specific target sum. One way to solve it is by checking all possible subsets (exponential time complexity). Although inefficient, this approach guarantees finding the correct subset if one exists.

```javascript
function isSubsetSum(set, n, target) {
    if (target === 0) {
        return true;
    }
    if (n === 0 && target !== 0) {
        return false;
    }
    if (set[n - 1] > target) {
        return isSubsetSum(set, n - 1, target);
    }
    return isSubsetSum(set, n - 1, target) || isSubsetSum(set, n - 1, target - set[n - 1]);
}

// Example usage
const inputSet = [3, 34, 4, 12, 5, 2];
const targetSum = 9;
const isSubsetPossible = isSubsetSum(inputSet, inputSet.length, targetSum);
console.log(`Subset with sum ${targetSum} exists: ${isSubsetPossible}`);

```

---

### Space Complexity

Space Complexity measures the amount of memory space an algorithm uses relative to the input size. Focused on how memory requirements increase, given the input size.

---

## The Four Rules in Big-O

* **Worst Case:** consider the worst case scenario (it doesn't matter if the value is found in the first interaction).
* **Remove Constants:** if I have three loops, respectively O(n + n/2 + 100), we only care when the inputs are getting larger, which leads us to O(n). Same for O(2n) --> O(n)
* **Different Terms for inputs:** if you iterate in two loops, for distinct arrays, we consider as different time complexities. Example:

```javascript
function combineArrays(arr1, arr2) {
    const combinedArray = [];

    // Loop through the first array (arr1): O(n)
    for (let i = 0; i < arr1.length; i++) {
        combinedArray.push(arr1[i]);
    }

    // Loop through the second array (arr2) O(m)
    for (let j = 0; j < arr2.length; j++) {
        combinedArray.push(arr2[j]);
    }

    return combinedArray;
}

// Example usage
const array1 = [1, 2, 3];
const array2 = [4, 5, 6];
const combined = combineArrays(array1, array2);
console.log("Combined Array:", combined); // O(n + m)

```

> In the example above, considering that each array is a different input, the result will be O(n + m).

* **Drop Non-Dominants:** consider the most relevant term in a mathematical experssion expression, dropping theless significant ones. Here is an example:

```javascript
function exampleFunction(n) {
    let quadraticTerm = 3 * n * n;  // Dominant term
    let linearTerm = 5 * n;
    let constantTerm = 2;

    let result = quadraticTerm + linearTerm + constantTerm;
    return result;
}

// Example usage
const inputSize = 10;
const output = exampleFunction(inputSize);
console.log("Output:", output);
```

> In this example, the function `exampleFunction(n)` has quadratic (n2**n****2**), linear (n**n**), and constant terms. However, when analyzing its time complexity, we focus on the dominant term (n2**n****2**) and drop the non-dominant linear and constant terms. The time complexity of this function is O(n2)**O****(****n****2****)** after dropping the non-dominant terms.

---

## Data Structures

A data structure is a way of organizing and storing data in a computer so that it can be accessed and manipulated efficiently. It defines the relationship between the data elements and enables operations to be performed on the data. Common data structures include arrays, linked lists, trees, and graphs.

### Arrays

#### Definition

An array is a collection of elements, all of the same data type, stored at contiguous memory locations. Each element in an array is identified by an index or a key.

#### Advantages

* **Fast Access Time:** Elements in an array can be accessed directly using their index, which allows for constant-time access. This means accessing any element in the array takes the same amount of time regardless of the size of the array.
* **Simplicity:** Arrays are simple and intuitive to use. They provide a straightforward way to store and retrieve data, making them easy to understand and implement.
* **Memory Efficiency:** Arrays have a contiguous memory allocation, which means they use memory efficiently. There is no overhead for storing pointers or references to other elements, as elements are stored sequentially in memory.
* **Cache Locality:** Due to contiguous memory storage, arrays exhibit good cache locality. Accessing elements that are close to each other in memory can utilize CPU caches effectively, improving performance.
* **Predictable Performance:** Array operations have predictable time complexity for accessing elements, making them suitable for applications where predictable performance is crucial.

#### Disadvantages

* **Fixed Size:** Arrays have a fixed size, meaning you need to specify the number of elements when you create them. Changing the size of an array (resizing) is often a costly operation, especially if the array is full, as it may require allocating a new, larger array and copying all elements.
* **Inefficient Insertions and Deletions:** Inserting or deleting elements in the middle of an array requires shifting elements, which can be computationally expensive, especially for large arrays. This operation has a time complexity of O(n), where n is the number of elements in the array.
* **Wasted Space:** If the size of the array is larger than the number of elements it holds, there can be wasted memory space, especially if the array size is fixed and larger than necessary.
* **Lack of Flexibility:** Arrays are not dynamic by default, meaning they cannot easily change in size at runtime. To work around this limitation, dynamic arrays (like ArrayList in Java or vectors in C++) or other data structures like linked lists are often used.
* **Non-Primitive Data Types:** In many programming languages, arrays can only store elements of the same data type. This limitation can be overcome by using arrays of objects or pointers, but it adds complexity to the code.

#### Use-Cases

**Storing and Manipulating Lists of Data:**

Arrays are widely used to store lists of data in JavaScript. For example, you can use an array to store a list of names, numbers, or any other type of data. You can easily add, remove, or modify elements in the array. For instance:

```javascript
// Storing a list of names in an array
let names = ["Alice", "Bob", "Charlie", "David"];

// Adding a new name to the array
names.push("Eva");

// Removing a name from the array
names.splice(2, 1); // Removes "Charlie" from the array

// Modifying an element in the array
names[1] = "Betty"; // Changes "Bob" to "Betty"

```

**Iterating and Processing Data:**
Arrays are perfect for iterating over elements and performing operations on each element. You can use loops like `for` or array methods like `forEach`, `map`, `filter`, and `reduce` to process the elements in an array. For example:

```javascript
// Calculating the sum of numbers in an array
let numbers = [1, 2, 3, 4, 5];
let sum = 0;

for (let i = 0; i < numbers.length; i++) {
  sum += numbers[i];
}

// Using array methods to calculate the sum
let sumUsingReduce = numbers.reduce((acc, current) => acc + current, 0);

```

**Implementing Data Structures and Algorithms:**

Arrays are fundamental for implementing various data structures like stacks, queues, and hash tables, as well as algorithms such as sorting and searching. For example, you can use an array as a stack by adding elements to the end and removing them from the end, implementing a Last In, First Out (LIFO) behavior. Similarly, you can use an array as a queue by adding elements to the end and removing them from the beginning, implementing a First In, First Out (FIFO) behavior.

```javascript
// Implementing a stack using an array
let stack = [];
stack.push(1); // Pushing an element onto the stack
let topElement = stack.pop(); // Popping an element from the stack

// Implementing a queue using an array
let queue = [];
queue.push(1); // Enqueue an element
let dequeuedElement = queue.shift(); // Dequeue an element

```

> In computer programming, arrays can be categorized as static or dynamic based on their size flexibility. Static arrays have a fixed size, determined at the time of declaration, while dynamic arrays can resize themselves to accommodate varying numbers of elements.
>
> When a dynamic array becomes full, it needs to resize itself to accommodate additional elements. A common resizing strategy involves doubling the array's size. However, this doubling strategy comes with a cost: copying all existing elements from the old array to a new, larger array in a different memory location. This copying operation ensures that there is enough contiguous space in memory to store the expanded array.

---

### Singly Linked Lists

#### Definition

A linear data structure where elements are stored in nodes, and each node points to the next element in the list. The **Singly Linked List**, a data structure where each element (node) contains data and a reference to the next element in a unidirectional sequence.

#### Advantages

* **Simple Implementation:** Singly linked lists are relatively simple to implement, making them easy to understand and use.
* **Memory Efficiency:** Singly linked lists are memory-efficient compared to doubly linked lists as they only require one pointer per node.
* **Dynamic Size:** Singly linked lists can easily adjust their size, allowing for dynamic addition or removal of elements without the need for pre-allocated memory.
* **Ease of Insertion and Deletion:** Inserting or deleting elements at the beginning of a singly linked list is a constant-time operation, making these operations efficient.
* **Straightforward Traversal::** Traversing a singly linked list is straightforward, moving from one node to the next using the next pointers.

#### Disadvantages

* **Limited Traversal Options:** Singly linked lists only support forward traversal, which can be a limitation in certain scenarios where backward traversal is necessary.
* **Inefficient Reverse Traversal:** Reversing a singly linked list is inefficient and often requires additional data structures or operations.
* **No Direct Access to Previous Node:** Accessing the previous node in a singly linked list requires traversing from the beginning of the list, leading to inefficiencies.
* **Memory Overhead for Large Lists:** In large singly linked lists, the memory overhead of storing next pointers for each node can become significant.
* **Limited Operations on Tail:** Performing operations at the end of a singly linked list, such as finding the tail or deleting the last node, can be less efficient compared to operations at the beginning.

#### Use-Cases

**Symbol Table in a Compiler:**

Building a symbol table in a compiler, where identifiers and their associated information are stored dynamically.

```javascript
class SymbolEntry {
  constructor(identifier, type) {
    this.identifier = identifier;
    this.type = type;
    this.next = null;
  }
}

class SymbolTable {
  constructor() {
    this.head = null;
  }

  addSymbol(identifier, type) {
    const newSymbol = new SymbolEntry(identifier, type);
    newSymbol.next = this.head;
    this.head = newSymbol;
  }

  findSymbol(identifier) {
    let current = this.head;

    while (current !== null) {
      if (current.identifier === identifier) {
        return current.type;
      }
      current = current.next;
    }

    return null; // Symbol not found
  }
}

// Example Usage:
const symbolTable = new SymbolTable();
symbolTable.addSymbol("variable1", "int");
symbolTable.addSymbol("variable2", "float");
console.log(symbolTable.findSymbol("variable1"));  // Output: int

```

---

### Doubly-Linked Lists

#### Definition

Doubly linked lists are a type of linked list where each node contains a data element and two pointers, one pointing to the next node in the sequence (next pointer) and another pointing to the previous node (previous pointer). This bidirectional linkage allows for more flexible traversal and manipulation compared to singly linked lists.

#### Advantages

* **Bidirectional Traversal:** Doubly linked lists support bidirectional traversal, allowing efficient movement in both forward and backward directions.

**Efficient Deletion:** Deleting a node in a doubly linked list is more efficient than in a singly linked list because the previous node's pointer is readily available.

**Reverse Traversal:** Reversing a doubly linked list is more efficient than in a singly linked list because each node has a pointer to its previous node.

**Dynamic Size with Tail Pointer:** A doubly linked list with a tail pointer allows for dynamic addition or removal of elements at both the beginning and end in constant time.

**Easier Implementation of Certain Algorithms:** Certain algorithms, such as reversing a linked list or detecting a palindrome, can be implemented more efficiently with a doubly linked list.

#### Disadvantages:

**Increased Memory Usage:** Doubly linked lists use more memory compared to singly linked lists because each node requires two pointers (next and previous).

**Complex Implementation:** Implementing and maintaining doubly linked lists is more complex than singly linked lists, leading to potentially more error-prone code.

**Memory Overhead for Large Lists:** In large doubly linked lists, the memory overhead of storing both next and previous pointers for each node can become significant.

**Limited Operations on Tail:** Although operations at the tail are more efficient than in a singly linked list, they are still less efficient than operations at the head.

**Increased Complexity for Certain Operations:** Some operations, such as insertion in the middle of the list, can be more complex and may require careful handling of multiple pointers.

#### Use-Cases

**Dynamic Task List:**
Managing a dynamic list of tasks with the ability to easily add or remove tasks.

```javascript
class Task {
  constructor(description) {
    this.description = description;
    this.next = null;
  }
}

class TaskList {
  constructor() {
    this.head = null;
  }

  addTask(description) {
    const newTask = new Task(description);
    newTask.next = this.head;
    this.head = newTask;
  }

  removeTask(description) {
    let current = this.head;
    let prev = null;

    while (current !== null) {
      if (current.description === description) {
        if (prev === null) {
          this.head = current.next;
        } else {
          prev.next = current.next;
        }
        return;
      }

      prev = current;
      current = current.next;
    }
  }
}

// Example Usage:
const tasks = new TaskList();
tasks.addTask("Complete assignment");
tasks.addTask("Read a book");
tasks.removeTask("Read a book");

```

**Undo/Redo Functionality:**

Implementing undo/redo functionality in applications where users can perform actions and revert them.

```javascript
class State {
  constructor(data, prevState = null) {
    this.data = data;
    this.prevState = prevState;
  }
}

class StateHistory {
  constructor() {
    this.currentState = null;
  }

  pushState(data) {
    this.currentState = new State(data, this.currentState);
  }

  undo() {
    if (this.currentState !== null) {
      this.currentState = this.currentState.prevState;
    }
  }

  getCurrentState() {
    return this.currentState ? this.currentState.data : null;
  }
}

// Example Usage:
const history = new StateHistory();
history.pushState("Initial State");
history.pushState("Updated State");
history.undo();
console.log(history.getCurrentState());  // Output: Initial State

```

**Symbol Table in a Compiler:**

Building a symbol table in a compiler, where identifiers and their associated information are stored dynamically.

```javascript
class SymbolEntry {
  constructor(identifier, type) {
    this.identifier = identifier;
    this.type = type;
    this.next = null;
  }
}

class SymbolTable {
  constructor() {
    this.head = null;
  }

  addSymbol(identifier, type) {
    const newSymbol = new SymbolEntry(identifier, type);
    newSymbol.next = this.head;
    this.head = newSymbol;
  }

  findSymbol(identifier) {
    let current = this.head;

    while (current !== null) {
      if (current.identifier === identifier) {
        return current.type;
      }
      current = current.next;
    }

    return null; // Symbol not found
  }
}

// Example Usage:
const symbolTable = new SymbolTable();
symbolTable.addSymbol("variable1", "int");
symbolTable.addSymbol("variable2", "float");
console.log(symbolTable.findSymbol("variable1"));  // Output: int

```

---

### Stacks

#### Definition

A stack is a linear data structure that follows the Last In, First Out (LIFO) principle, where elements are added and removed from the same end, typically referred to as the "top." New elements are pushed onto the top, and only the top element can be popped or accessed at any given time.

#### Advantages

* **Simple Implementation:** Stacks are simple to implement, making them easy to understand and use.
* **Efficient Push and Pop Operations:** Adding and removing elements from the top of the stack (push and pop operations) have constant time complexity.
* **Space Efficiency:** Stacks can be more memory-efficient than dynamic data structures like linked lists because they have a fixed size.
* **Support for Undo Mechanism:** Stacks are commonly used to implement undo mechanisms in software applications.
* **Function Call Management:** Stacks are used in programming languages to manage function calls and store local variables.

#### Disadvantages

* **Limited Access:** Stacks offer limited access to elements. Only the top element can be directly accessed.
* **Fixed Size:** Traditional stacks have a fixed size, and resizing can be challenging, leading to potential overflow or underflow issues.
* **Not Suitable for Random Access:** Stacks are not suitable for scenarios where random access to elements is required.
* **Memory Management Overhead:** Stacks may have memory management overhead due to their fixed size, even if the stack is not full.
* **Limited Applicability:** Stacks are best suited for specific scenarios like managing function calls or undo mechanisms and may not be the most efficient choice for other data access patterns

#### Use-Cases

---

### Queues

#### Definition

A queue is a linear data structure that follows the First In, First Out (FIFO) principle, where elements are added at the rear and removed from the front. It operates like a waiting line, ensuring that the first element enqueued is the first to be dequeued.

#### Advantages

* **Efficient Enqueue and Dequeue Operations:** Adding and removing elements from the front and rear of the queue (enqueue and dequeue operations) have constant time complexity in well-implemented queues.
* **FIFO Order:** Queues follow the First In, First Out (FIFO) principle, ensuring that elements are processed in the order they were added.
* **Memory Efficiency:** Queues can be more memory-efficient than dynamic data structures like linked lists because they have a fixed size.
* **Task Scheduling:** Queues are commonly used in task scheduling and management systems, ensuring tasks are processed in a fair order.
* **Buffering:** Queues are employed in scenarios where data needs to be buffered or smoothed out, such as in communication systems.

#### Disadvantages

* **Limited Access:** Queues offer limited access to elements. Only the front and rear elements can be directly accessed.
* **Fixed Size:** Traditional queues have a fixed size, and resizing can be challenging, leading to potential overflow or underflow issues.
* **Not Suitable for Random Access:** Queues are not suitable for scenarios where random access to elements is required.
* **Memory Management Overhead:** Queues may have memory management overhead due to their fixed size, even if the queue is not full.
* **Limited Applicability:** Queues are best suited for specific scenarios like task scheduling or buffering and may not be the most efficient choice for other data access patterns.

#### Use-Cases

---

### Hash Tables

#### Definition

A data structure that stores key-value pairs and uses a hash function to compute an index into an array where the corresponding value can be found. A hash table is a data structure that implements an associative array abstract data type, providing efficient access and storage of key-value pairs through a hash function. It enables rapid lookup, insertion, and deletion operations with average-case constant time complexity.

#### Advantages

* **Fast Lookup:** Hash tables offer fast average-case lookup times, providing constant-time or near-constant-time access to stored elements.
* **Efficient Insertion and Deletion:** Inserting and deleting elements in a well-designed hash table can also be performed in constant time on average.
* **Adaptability to Dynamic Data:** Hash tables can dynamically adjust to changing data sizes without a significant increase in average-case time complexity.
* **Effective for Search Operations:** Hash tables are highly effective for search operations when the key is known, making them suitable for applications like databases and caches.
* **Optimized Memory Usage:** When designed well, hash tables can offer optimized memory usage, reducing the likelihood of collisions.

#### Disadvantages

* **Potential for Collisions:** Hash collisions can occur when two different keys produce the same hash value, requiring additional handling mechanisms like chaining or open addressing.
* **Hash Function Dependency:** The efficiency of a hash table relies heavily on the quality of the hash function, and a poor hash function may lead to increased collisions.
* **Unordered Output:** The ordering of elements in a hash table is not deterministic and does not follow a specific order, making it unsuitable for scenarios requiring ordered traversal.
* **Complexity of Implementation:** Designing an efficient and collision-resistant hash table can be complex, requiring careful consideration of the hash function, collision resolution strategy, and load factor.
* **Space Overhead:** Hash tables may have a space overhead due to potential unused slots and the need for additional data structures to handle collisions.

#### Use-Cases

---

### Trees

#### Definition

A tree is a hierarchical data structure composed of **nodes**, where each node contains a value and may have **zero or more child nodes**, forming a branching structure. The topmost node in a tree is called the **root**, and nodes with no children are called **leaves**. Nodes in a tree are connected by **edges**, and the relationship between nodes reflects a hierarchical arrangement. Trees are widely used in computer science for representing hierarchical relationships, organizing data, and supporting various algorithms and data storage structures.

#### Advantages

* **Hierarchical Organization:** Trees provide a hierarchical structure, allowing for the representation of parent-child relationships among elements.
* **Efficient Search Operations:** Binary search trees, in particular, enable efficient search operations with average-case logarithmic time complexity.
* **Natural Representation of Hierarchies:** Trees naturally represent hierarchical relationships, making them suitable for modeling organizational structures, file systems, and other hierarchical entities.
* **Efficient Insertion and Deletion:** Balanced trees, such as AVL trees and Red-Black trees, offer efficient insertion and deletion operations with logarithmic time complexity.
* **Versatility in Applications:** Trees are versatile and find applications in various domains, including databases, expression evaluation, decision-making processes, and network routing algorithms.

#### Disadvantages

* **Complexity of Implementation:** Designing and implementing certain types of trees, especially balanced ones, can be complex and may require careful consideration of balancing criteria.
* **Potential for Skewed Trees:** Unbalanced trees can lead to performance degradation, particularly in search operations, with worst-case linear time complexity.
* **Memory Overhead:** Trees may have a memory overhead due to the storage of additional pointers or metadata for maintaining the hierarchical structure.
* **Difficulty in Ordered Traversal:** Some types of trees, like general trees, do not provide a natural ordering of elements, making ordered traversal challenging.
* **Limited Applicability for Unrelated Data:** Trees are most effective when representing hierarchical relationships, and their use may be less intuitive for representing unrelated or non-hierarchical data.

#### Use-Cases

---

### Graphs

#### Definition

Graphs are a fundamental data structure in computer science and mathematics. They consist of a collection of **nodes (vertices)** and **edges **that connect pairs of nodes. The connections between nodes represent relationships or interactions between the associated entities.

### **Advantages:**

* **Versatility:** Graphs provide a versatile way to represent and model various relationships, from social networks and transportation systems to computer networks and dependencies in software.
* **Efficient Representation:** Certain relationships, such as connectivity or pairwise interactions, can be efficiently represented and analyzed using graph structures.
* **Traversal and Pathfinding:** Graph algorithms, such as depth-first search (DFS) and breadth-first search (BFS), are effective for traversing and finding paths in a graph.
* **Cyclic Relationships:** Graphs can represent cyclic relationships, making them suitable for modeling scenarios where elements can have mutual connections.
* **Hierarchical Representation:** Trees are a specific type of graph, providing a hierarchical representation, making them suitable for hierarchical structures like file systems.

### **Disadvantages:**

* **Complexity of Algorithms:** Some graph algorithms, especially those dealing with cyclic graphs or graphs with complex relationships, can be computationally expensive.
* **Memory Consumption:** Depending on the implementation, graphs may require significant memory, especially for large or dense graphs.
* **Lack of Natural Ordering:** Graphs do not inherently provide a natural ordering of elements, which may be a disadvantage in scenarios where ordered traversal is essential.
* **Potential for Ambiguity:** In some cases, the relationships modeled by a graph may introduce ambiguity, requiring additional context for interpretation.
* **Complexity in Representing Certain Relationships:** While versatile, graphs may not be the most intuitive representation for certain relationships, and other data structures may be more appropriate.

#### Use-Cases

---

## Recursion

Recursion is a programming technique where a function calls itself, either directly or indirectly, to solve a smaller instance of the same problem. This process continues until a base case is reached, providing a solution for the original problem by combining solutions from the smaller instances. Recursion is often used to simplify the implementation of certain algorithms, make code more readable, and handle problems with inherent recursive structures.

### **Advantages**

* **Simplicity and Readability:** Recursive solutions often result in more concise and readable code, mirroring the natural structure of the problem.
* **Reduced Complexity:** Recursion can simplify complex problems by breaking them down into smaller, more manageable sub-problems, leading to clearer overall logic.
* **Divide and Conquer:** Recursive solutions often follow a "divide and conquer" approach, dividing a problem into smaller sub-problems, making them easier to solve.
* **Elegant Implementation:** Certain problems have elegant and natural recursive solutions, especially those involving hierarchical structures.
* **Modular Design:** Recursive functions promote modular design, encapsulating specific tasks or logic within functions, enhancing code organization.

### **Disadvantages**

* **Stack Overflow:** Excessive recursive calls can lead to a stack overflow, limiting the practicality of recursion for problems with large input sizes.
* **Memory Overhead:** Each recursive call adds a new frame to the call stack, potentially leading to high memory usage, particularly with deep recursion.
* **Performance:** Recursive solutions might be less performant than iterative counterparts due to the overhead of function calls and stack management.
* **Difficulty in Debugging:** Recursive code can be challenging to debug, especially for complex problems, making bug identification and fixing more difficult.
* **Potential for Infinite Recursion:** Incorrectly implemented recursion may result in infinite loops, causing the program to hang or crash.

---

## Sorting Algorithms

Sorting algorithms are specific algorithms designed to arrange elements in a specific order, often numerically or alphabetically. These algorithms systematically reorder items within a list or an array, making it easier to search for specific elements or analyze data. Various sorting algorithms, such as bubble sort, merge sort, and quicksort, employ different techniques to efficiently organize data, each with its own advantages and trade-offs in terms of time and space complexity. Sorting algorithms are fundamental in computer science and are extensively used in various applications, including databases, search algorithms, and data analysis.

### Bubble Sort

**Definition**

Bubble Sort is a simple sorting algorithm that repeatedly steps through the list, compares adjacent elements, and swaps them if they are in the wrong order. The pass through the list is repeated until no swaps are needed, indicating that the list is sorted. It is named for the way smaller elements "bubble" to the top of the list during each iteration.

**Advantages:**

* **Simplicity:** Bubble Sort is easy to understand and implement, making it a good choice for educational purposes or small datasets.
* **In-Place Sorting:** It only requires a constant amount of additional memory for swapping elements, making it an in-place sorting algorithm.

**Disadvantages:**

* **Inefficiency with Large Datasets:** Bubble Sort has a time complexity of O(n^2), making it inefficient for large datasets.
* **Lack of Adaptivity:** The algorithm doesn't adapt to the existing order in the list. It performs the same number of comparisons even if the list is partially sorted.
* **Poor Performance:** Bubble Sort's performance is poor compared to more advanced sorting algorithms like QuickSort or MergeSort.
* **Not Suitable for Real-world Applications:** Due to its inefficiency, it's seldom used in real-world applications where sorting large datasets is a common requirement.

---

### Selection Sort

**Definition**

Selection Sort is a simple sorting algorithm that repeatedly selects the minimum element from an unsorted portion of the list and swaps it with the first unsorted element. This process is repeated until the entire
list is sorted. It has a time complexity of O(n^2) and is generally used for educational purposes or on small datasets due to its inefficiency for larger sets.

**Advantages:**

* **Simplicity:** Selection Sort is straightforward to understand and implement, making it suitable for educational purposes or small datasets.
* **In-Place Sorting:** It sorts the elements in-place, meaning it doesn't require additional memory for storage.

**Disadvantages:**

* **Inefficiency with Large Datasets:** Selection Sort has a time complexity of O(n^2), making it inefficient for large datasets.
* **Lack of Adaptivity:** The algorithm doesn't adapt to the existing order in the list. It performs the same number of comparisons even if the list is partially sorted.
* **Unstable Sorting:** Selection Sort is not a stable sorting algorithm, meaning it may change the relative order of equal elements.
* **Poor Performance:** Selection Sort's performance is poor compared to more advanced sorting algorithms like QuickSort or MergeSort.
* **Not Suitable for Real-world Applications:** Due to its inefficiency, it's seldom used in real-world applications where sorting large datasets is a common requirement.

---

### Insertion Sort

#### Definition

Insertion Sort is a straightforward sorting algorithm that builds the final sorted array one item at a time. It iterates through the input array, taking one element at each step and inserting it into its correct position relative to the already sorted elements. The algorithm is efficient for small datasets but less practical for larger ones due to its time complexity of O(n^2).


* **Advantages:**

  * **Simple Implementation:** Insertion Sort is relatively easy to understand and implement, making it suitable for educational purposes or small datasets.
  * **Efficient for Small Datasets:** It performs well with small datasets and is often faster than more complex algorithms for lists of limited size.
* **Disadvantages:**

  * **Inefficiency with Large Datasets:** Insertion Sort has a time complexity of O(n^2), making it inefficient for large datasets.
  * **Poor Performance:** Insertion Sort's performance is poor compared to more advanced sorting algorithms like QuickSort or MergeSort.
  * **Not Suitable for Real-world Applications:** Due to its inefficiency, it's seldom used in real-world applications where sorting large datasets is a common requirement.
* **Advantages:**

  * **Simple Implementation:** Insertion Sort is relatively easy to understand and implement, making it suitable for educational purposes or small datasets.
  * **Efficient for Small Datasets:** Performs well with small datasets and is often faster than more complex algorithms for lists of limited size.
  * **Stable Sorting:** Maintains the relative order of equal elements, making it a stable sorting algorithm.
  * **Adaptive:** Takes advantage of existing order, with a best-case time complexity of O(n) when the input is nearly sorted.
* **Disadvantages:**

  * **Inefficiency with Large Datasets:** Insertion Sort has a time complexity of O(n^2), making it inefficient for large datasets.
  * **Unstable for Large Datasets:** Despite being stable and adaptive, its performance degrades for larger datasets compared to more advanced sorting algorithms.
  * **Not Suitable for Real-world Applications:** Due to its inefficiency, it's seldom used in real-world applications where sorting large datasets is a common requirement

---

### Merge Sort

#### Definition

Merge Sort is a divide-and-conquer sorting algorithm that recursively divides the input array into smaller halves, sorts them individually, and then merges the sorted halves to produce the final sorted array. It has a stable and consistent time complexity of O(n log n).

---

### Quick Sort

#### Definition

Quick Sort is a divide-and-conquer sorting algorithm that selects a "pivot" element from the array, partitions the other elements into two sub-arrays based on whether they are less than or greater than the pivot, and then recursively sorts the sub-arrays. It is an in-place and efficient algorithm with an average-case time complexity of O(n log n).

---

### Heap Sort

#### Definition

Heap Sort is a comparison-based sorting algorithm that uses a binary heap data structure to create a partially ordered binary tree. It repeatedly extracts the maximum element from the heap, swaps it with the last element, and maintains the heap property. It has a time complexity of O(n log n) and is an in-place sorting algorithm.

---

### Radix Sort

#### Definition

Radix Sort is a non-comparative sorting algorithm that works by distributing elements into buckets based on individual digits or radix positions. It processes the digits from the least significant to the most significant or vice versa. Radix Sort is suitable for sorting integers or strings with fixed-length representations and has a linear time complexity in certain scenarios.

---

## Searching Algorithms

Searching algorithms are algorithms designed to locate a specific item or a particular value within a collection of data. These algorithms systematically explore the data, looking for the target element and determining its presence or absence. Common searching algorithms include linear search (sequential search) and binary search. Linear search checks each element in the data structure until it finds the target, while binary search works on sorted data by repeatedly dividing the search interval in half. Searching algorithms are crucial for tasks like finding specific records in databases, locating elements in arrays, and enabling efficient search functionality in applications and websites. They play a vital role in information retrieval and data processing algorithms.

### Linear Search

#### Definition

---

### Binary Search

#### Definition

---

### Breadth-First Search (BFS)

#### Definition

---

### Depth-First Search (DFS)

#### Definition

---

## Links

[Big-O Complexity Chart](https://www.bigocheatsheet.com/)

[Data Structures + Algorithms (Udemy)](https://www.udemy.com/course/master-the-coding-interview-data-structures-algorithms/)

[Visualgo.NET](https://visualgo.net)

[Repl](https://replit.com)

[Top 8 Data Structures for Coding Interviews](https://dev.to/fahimulhaq/top-8-data-structures-for-coding-interviews-and-practice-interview-questions-2pb)

[Sorting Algorithms Animations](https://www.toptal.com/developers/sorting-algorithms)
