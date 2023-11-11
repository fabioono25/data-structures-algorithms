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
