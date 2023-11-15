// Doubly-linked lists (definition): a linked list that has a pointer to the previous node
// Doubly-linked lists (pros): can be iterated in both directions
// Doubly-linked lists (cons): more memory, more complex code

class Node {
  constructor(value) {
    this.value = value;
    this.next = null;
    this.prev = null; // new
  }
}

class DoublyLinkedList {
  constructor(value) {
    this.head = new Node(value); // the head and tail are the same node
    this.tail = this.head;
    this.length = 1;
  }

  append(value) { // O(1)
    const newNode = new Node(value);
    newNode.prev = this.tail; // new
    this.tail.next = newNode;
    this.tail = newNode;
    this.length++;
    return this;
  }

  prepend(value) { // O(1)
    const newNode = new Node(value);
    newNode.next = this.head;
    this.head = newNode;
    this.head.prev = newNode; // new
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
    const follower = leader.next;
    leader.next = newNode;
    newNode.prev = leader;
    newNode.next = follower;
    follower.prev = newNode;
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
    leader.prev = unwantedNode.prev; // new
    this.length--;
    return this;
  }
}

const myDoublyLinkedList = new DoublyLinkedList(10);
myDoublyLinkedList.print();
myDoublyLinkedList.append(5);
myDoublyLinkedList.append(16);
myDoublyLinkedList.print();
myDoublyLinkedList.prepend(1);
myDoublyLinkedList.print();
myDoublyLinkedList.insert(2, 99);
myDoublyLinkedList.print();
myDoublyLinkedList.remove(2);
myDoublyLinkedList.print();