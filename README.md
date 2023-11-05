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

### Space Complexity

Space Complexity measures the amount of memory space an algorithm uses relative to the input size. Focused on how memory requirements increase, given the input size.

### Links

[Big-O Complexity Chart](https://www.bigocheatsheet.com/)
