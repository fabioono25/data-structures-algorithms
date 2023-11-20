// Graphs definition: A data structure that consists of nodes and connections
// Used to model things like social networks, location/mapping, routing algorithms
// A collection of nodes and connections between those nodes
// Nodes are also called vertices
// Connections are also called edges
// Unlike trees, graphs can be nonlinear

class Graph {
  constructor() {
    this.numberOfNodes = 0;
    this.adjacentList = {};
  }

  // Add a node
  addVertex(node) {
    this.adjacentList[node] = [];
    this.numberOfNodes++;
  }

  // Add an edge
  addEdge(node1, node2) {
    // Undirected Graph
    this.adjacentList[node1].push(node2);
    this.adjacentList[node2].push(node1);
  }

  showConnections() {
    for (let node in this.adjacentList) {
      let connections = this.adjacentList[node];
      let connectionsString = "";

      for (let connection of connections) {
        connectionsString += connection + " ";
      }

      console.log(node + " --> " + connectionsString);
    }
  }
}

var myGraph = new Graph();
myGraph.addVertex("0");
myGraph.addVertex("1");
myGraph.addVertex("2");
myGraph.addVertex("3");
myGraph.addVertex("4");
myGraph.addVertex("5");
myGraph.addVertex("6");
myGraph.addEdge("3", "1");
myGraph.addEdge("3", "4");
myGraph.addEdge("4", "2");
myGraph.addEdge("4", "5");
myGraph.addEdge("1", "2");
myGraph.addEdge("1", "0");
myGraph.addEdge("0", "2");
myGraph.addEdge("6", "5");

myGraph.showConnections();
