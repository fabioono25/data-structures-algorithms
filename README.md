# Data Structures and Algorithms - JavaScript

## Big O Notation

A mathematical notation used in computer science to describe performance and complexity of an algorithm.

![](assets/20231105_122936_bigO.png)

### Time Complexity

Time Complexity measures the amount of time an algorithm takes to run as a function of the input size. Focused on how the execution time increases, given the input size.

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

#### The Four Rules in Big-O

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

* Drop Non-Dominants:**

---

### Space Complexity

Space Complexity measures the amount of memory space an algorithm uses relative to the input size. Focused on how memory requirements increase, given the input size.

### Links

[Big-O Complexity Chart](https://www.bigocheatsheet.com/)
