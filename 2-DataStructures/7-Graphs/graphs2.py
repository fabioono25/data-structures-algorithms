from collections import deque  # structure: FIFO queue. Used for BFS


class Node:
    def __init__(self, value):
        self.value = value
        self.adjacent = []  # list of nodes (edges)

    def add_neighbor(self, neighbor):
        if neighbor not in self.adjacent:
            self.adjacent.append(neighbor)

    def show_connections(self):
        for node in self.adjacent:
            print(node.value, end=' ')
        print()


class Graph:
    def __init__(self):
        # self.nodes = []
        self.nodes = {}

    def add_node(self, value):
        if value not in self.nodes:
            self.nodes[value] = Node(value)

    def add_edge(self, from_value, to_value):
        self.add_node(from_value)
        self.add_node(to_value)
        self.nodes[from_value].add_neighbor(self.nodes[to_value])

    def get_node(self, value):
        return self.nodes.get(value)

    def bfs(self, start_value):
        visited = set()
        queue = deque([self.get_node(start_value)])

        while queue:
            node = queue.popleft()
            if node.value not in visited:
                visited.add(node.value)
                for neighbor in node.adjacent:
                    queue.append(neighbor)
        return visited

    def dfs(self, start_value):
        visited = set()
        stack = [self.get_node(start_value)]

        while stack:
            node = stack.pop()
            if node.value not in visited:
                visited.add(node.value)
                for neighbor in node.adjacent[::-1]:
                    if neighbor not in visited:
                        stack.append(neighbor)
            return visited

    def dfs_recursive(self, start_value):
        visited = set()

        def dfs_util(node):
            visited.add(node.value)
            print(node.value)
            for neighbor in node.adjacent:
                if neighbor.value not in visited:  # Check if neighbor's value is in visited
                    dfs_util(neighbor)

        start_node = self.get_node(start_value)
        dfs_util(start_node)




# testing
node1 = Node('0')
node2 = Node('1')
node3 = Node('2')
node1.add_neighbor(node2)
node1.add_neighbor(node3)
node1.show_connections()

graph = Graph()
graph.add_edge(0, 1)
graph.add_edge(0, 2)
graph.add_edge(1, 2)
graph.add_edge(2, 0)
graph.add_edge(2, 3)
graph.add_edge(3, 3)

print("BFS:")
print(graph.bfs(2))
print("DFS:")
print(graph.dfs(2))
print("DFS (Recursive):")
graph.dfs_recursive(2)
