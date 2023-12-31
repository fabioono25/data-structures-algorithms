// queue definition: FIFO (First In First Out)
// queue operations: enqueue, dequeue, peek, length
//

// 1. Create a queue [using Linked List]
class Node {
  constructor(data) {
    this.data = data;
    this.next = null;
  }
}

class Queue {
  constructor() {
    this.first = null;
    this.last = null;
    this.length = 0;
  }

  peek() {
    return this.first;
  }

  enqueue(value) {
    const newNode = new Node(value);

    if (this.length === 0) {
      this.first = newNode;
      this.last = newNode;
    } else {
      this.last.next = newNode;
      this.last = newNode;
    }
    this.length++;
    return this
  }

  dequeue() {
    if (!this.first) {
      return null;
    }

    if (this.first === this.last) {
      this.last = null;
    }

    this.first = this.first.next;
    this.length--;
    return this;
  }
}

// 2. Create a queue [using Array]
class QueueArrays {
  constructur() {
    this.array = [];
  }

  peek() {
    return this.array[0];
  }

  enqueue(value) {
    this.array.push(value);
    return this;
  }

  dequeue() {
    this.array.pop();
    return this;
  }
}

const myQueue = new Queue();
myQueue.enqueue('Joy');
myQueue.enqueue('Matt');
myQueue.enqueue('Pavel');
myQueue.enqueue('Samir');
console.log(myQueue.peek());
console.log(myQueue.dequeue());
console.log(myQueue.peek());

const myQueueArray = new Queue();
myQueue.enqueue('Joy');
myQueue.enqueue('Matt');
myQueue.enqueue('Pavel');
myQueue.enqueue('Samir');
console.log(myQueue.peek());
console.log(myQueue.dequeue());
console.log(myQueue.peek());