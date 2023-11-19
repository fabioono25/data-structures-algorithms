// Trees definition: A data structure that consists of nodes in a parent/child relationship
// Trees are nonlinear, unlike linked lists, stacks, and queues
// Trees are used to model things like file directories, organization charts, etc
// A tree consists of a root node and child nodes
// A node can have a reference to a parent node
// A node can have multiple children
// A node with no children is called a leaf node
// A node with children is called an internal node
// A tree can have multiple roots
// A tree can have multiple levels
// A tree is a special type of graph
// A tree is a type of graph, but not all graphs are trees
// A tree is a connected graph without cycles
// level 0: 2^0 = 1 node. level 1: 2^1 = 2 nodes. level 2: 2^2 = 4 nodes. level 3: 2^3 = 8 nodes
// log 100 = 2 ==> 10 ^ 2 = 100

function BinaryTree(value) {
  this.value = value;
  this.left = null;
  this.right = null;
}