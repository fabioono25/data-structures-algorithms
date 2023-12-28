# DFS definition: it is a graph search algorithm that begins at the root node and explores as far as possible along each branch before backtracking.
# Time complexity: O(V+E) where V is the number of vertices in the graph and E is the number of edges in the graph.
# Space complexity: O(V) where V is the number of vertices in the graph.
# Examples of use: social networking, network broadcast, garbage collection, model checking, solving puzzles and games, finding shortest path, etc.

class Node:
    def __init__(self, name):
        self.name = name
        self.adjacencyList = []  # represents the neighbors of the node
        self.visited = False
        self.predecessor = None


def dfs(startNode):
    stack = [startNode]

    while stack:
        actualNode = stack.pop()  # pop the last element of the list
        actualNode.visited = True
        print("%s " % actualNode.name)

        for n in actualNode.adjacencyList:  # iterate over the neighbors of the node
            if not n.visited:
                n.visited = True
                stack.append(n)

if __name__ == "__main__":
    # create nodes
    node1 = Node("A")
    node2 = Node("B")
    node3 = Node("C")
    node4 = Node("D")
    node5 = Node("E")

    # create edges
    node1.adjacencyList.append(node2)
    node1.adjacencyList.append(node3)
    node2.adjacencyList.append(node4)
    node4.adjacencyList.append(node5)

    # run dfs
    dfs(node1)
