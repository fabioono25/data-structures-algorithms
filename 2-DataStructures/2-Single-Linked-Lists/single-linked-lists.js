// Linked Lists is a data structure that contains a head, tail and length property.
// Linked Lists consist of nodes, and each node has a value and a pointer to another node or null.
// Linked Lists do not have indexes.
// Linked Lists are an excellent alternative to arrays when insertion and deletion at the beginning are frequently required.
// Arrays contain a built in index whereas Linked Lists do not.
// The idea of a list data structure that consists of nodes is the foundation for other data structures like Stacks and Queues.

const basket = ['apples', 'grapes', 'pears'];
// apples
// 8947 --> grapes
//           8742 --> pears
//                     372 --> null

// playing with pointer references:
let obj1 = { a: true };
let obj2 = obj1;
obj1.a = 'changed';
console.log('obj1', obj1);
console.log('obj2', obj2);
delete obj1;
// console.log('obj1', obj1);
console.log('obj2', obj2); // there is still a pointer to this point in memory

// building a linked list from scratch
class Node {
  constructor(value) {
    this.value = value;
    this.next = null;
  }
}

class LinkedList {
  constructor(value) {
    this.head = new Node(value); // the head and tail are the same node
    this.tail = this.head;
    this.length = 1;
  }

  append(value) { // O(1)
    const newNode = new Node(value);
    this.tail.next = newNode;
    this.tail = newNode;
    this.length++;
    return this;
  }

  prepend(value) { // O(1)
    const newNode = new Node(value);
    newNode.next = this.head;
    this.head = newNode;
    this.length++;
    return this;
  }

  insert(index, value) { // O(n)
    if (index >= this.length) {
      return this.append(value);
    }
    if (index === 0) {
      return this.prepend(value);
    }
    const newNode = new Node(value);
    const leader = this.traverseToIndex(index - 1);
    const holdingPointer = leader.next;
    leader.next = newNode;
    newNode.next = holdingPointer;
    this.length++;
    return this;
  }

  traverseToIndex(index) { // O(n)
    let counter = 0;
    let currentNode = this.head;
    while (counter !== index) {
      currentNode = currentNode.next;
      counter++;
    }
    return currentNode;
  }

  print() {
    const array = [];
    let currentNode = this.head;
    while (currentNode !== null) {
      array.push(currentNode.value)
      currentNode = currentNode.next;
    }
    console.log(array);
  }

  remove(index) { // O(n)
    if (index === 0) {
      this.head = this.head.next;
      this.length--;
      return this;
    }
    if (index >= this.length) {
      index = this.length - 1;
    }
    const leader = this.traverseToIndex(index - 1);
    const unwantedNode = leader.next;
    leader.next = unwantedNode.next;
    this.length--;
    return this;
  }

  reverse() { // O(n)
    if (!this.head.next) {
      return this.head;
    }
    let first = this.head;
    this.tail = this.head;
    let second = first.next;
    while(second) {
      const temp = second.next; // save the next node
      second.next = first; // reverse the pointer
      first = second; // move the pointers forward
      second = temp;
    }
    this.head.next = null;
    this.head = first;
    return this;
  }
}

const myLinkedList = new LinkedList(10);
myLinkedList.append(5);
myLinkedList.append(16);
myLinkedList.prepend(1);
myLinkedList.insert(2, 99);
myLinkedList.remove(2);
myLinkedList.print();
myLinkedList.reverse();
myLinkedList.print();

// 10 --> 5 --> 16
let linkedList = {
  head: {
    value: 10,
    next: {
      value: 5,
      next: {
        value: 16,
        next: null,
      }
    }
  }
}