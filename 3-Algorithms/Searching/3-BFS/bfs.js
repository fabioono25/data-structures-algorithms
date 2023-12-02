// Breadth First Search (BFS) definition: traverses a graph in a breadthward motion and uses a queue to remember to get the next vertex to start a search, when a dead end occurs in any iteration.
// Time complexity: O(V+E) where V is number of vertices in the graph and E is number of edges in the graph.
// Space Complexity: O(V)

class Graph {
  constructor() {
    this.adjacencyList = new Map();
  }

  addNode(node) {
    this.adjacencyList.set(node, []);
  }

  addEdge(node1, node2) {
    this.adjacencyList.get(node1).push(node2);
    this.adjacencyList.get(node2).push(node1); // For undirected graph
  }

  bfs(startNode) {
    const visited = new Set();
    const queue = [];

    queue.push(startNode);
    visited.add(startNode);

    while (queue.length > 0) {
      const currentNode = queue.shift();
      console.log(`Visited Node: ${currentNode}`);

      const neighbors = this.adjacencyList.get(currentNode);
      for (const neighbor of neighbors) {
        if (!visited.has(neighbor)) {
          queue.push(neighbor);
          visited.add(neighbor);
        }
      }
    }
  }
}

// Example Usage:
const graph = new Graph();

graph.addNode("A");
graph.addNode("B");
graph.addNode("C");
graph.addNode("D");
graph.addNode("E");

graph.addEdge("A", "B");
graph.addEdge("A", "C");
graph.addEdge("B", "D");
graph.addEdge("C", "E");

console.log("BFS Traversal:");
graph.bfs("A");
