// Stack definition: LIFO (Last In First Out)
// Stack operations: push, pop, peek, length

// 1. Create a stack [using Linked List]
class Node {
  constructor(data) {
    this.data = data;
    this.next = null;
  }
}

class Stack {
  constructor() {
    this.top = null;
    this.bottom = null;
    this.length = 0;
  }

  peek() {
    return this.top;
  }

  push(value) {
    const newNode = new Node(value);

    if (this.length === 0) {
      this.top = newNode;
      this.bottom = newNode;
    } else {
      const holdingPointer = this.top;
      this.top = newNode;
      this.top.next = holdingPointer;
    }
    this.length++;
    return this;
  }

  pop() {
    if (!this.top) {
      return null;
    }

    const holdingPointer = this.top;
    this.top = this.top.next;
    this.length--;
  }
}

// 2. Create a stack [using Array]
class StackArray {
  constructor() {
    this.array = [];
  }

  peek() {
    return this.array[this.array.length - 1];
  }

  push(value) {
    this.array.push(value);
    return this;
  }

  pop() {
    // if (this.array.length === 0) {
    //   return null;
    // }

    // this.array = this.array.slice(0, this.array.length - 2);
    // return this;
    this.array.pop();
    return this;
  }
}

const myStack = new Stack();
console.log("WORKING WITH LINKED LIST");
myStack.push("google");
myStack.push("udemy");
myStack.push("discord");
console.log(myStack.peek());
myStack.pop();
console.log(myStack.peek());

console.log("WORKING WITH ARRAY");
const myStackArray = new StackArray();
myStack.push("google");
myStack.push("udemy");
myStack.push("discord");
console.log(myStack.peek());
myStack.pop();
console.log(myStack.peek());


