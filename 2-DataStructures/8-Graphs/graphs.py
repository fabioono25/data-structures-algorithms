# Graphs definition: it is a collection of nodes (vertices) along with
# identified pairs of nodes (called edges, links, etc).
# Graphs are used to represent networks.
# Graphs are used to represent roads, flights, social media, etc.
# Graphs are used to represent maps.
# Graphs are used to represent recommendations.

# example
class Graph: 
    def __init__(self):
        self.numberOfNodes = 0
        self.adjacentList = {}

    def addVertex(self, node):
        self.adjacentList[node] = []
        self.numberOfNodes += 1

    def addEdge(self, node1, node2):
        # undirected Graph 
        self.adjacentList[node1].append(node2)
        self.adjacentList[node2].append(node1)

    def showConnections(self):
        for node in self.adjacentList:
            print(node, end='-->')
            for vertex in self.adjacentList[node]:
                print(vertex, end=' ')
            print()

# testing
myGraph = Graph()
myGraph.addVertex('0')
myGraph.addVertex('1')
myGraph.addVertex('2')
myGraph.addVertex('3')
myGraph.addVertex('4')
myGraph.addVertex('5')
myGraph.addVertex('6')
myGraph.addEdge('3', '1')
myGraph.addEdge('3', '4')
myGraph.addEdge('4', '2')
myGraph.addEdge('4', '5')
myGraph.addEdge('1', '2')
myGraph.addEdge('1', '0')
myGraph.addEdge('0', '2')
myGraph.addEdge('6', '5')
myGraph.showConnections()
