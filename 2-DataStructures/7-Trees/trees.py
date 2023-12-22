# Trees Definition: A tree is a collection of nodes and edges. It is a non-linear data structure.
# It has a root node and each node has zero or more child nodes.
# Each child node has zero or more child nodes, and so on.
# A node is called a “leaf” node if it has no children.
# A tree is called “empty” if it contains no nodes.
# operations: insert, delete, search, traverse

class Tree:
    def __init__(self, value):
        self.value = value
        self.children = []

    def add_child(self, value):
        self.children.append(Tree(value))

    def remove_child(self, value):
        self.children = [child for child in self.children if child.value != value]

    def traverse(self):
        nodes = [self]
        while len(nodes) > 0:
            current_node = nodes.pop()
            print(current_node.value)
            nodes += current_node.children[::-1]

    def search(self, value):
        nodes = [self]
        while len(nodes) > 0:
            current_node = nodes.pop()
            if current_node.value == value:
                return True
            nodes += current_node.children[::-1]
        return False

# testing
tree = Tree("Drinks")
tree.add_child("Hot")
tree.add_child("Cold")
tree.children[0].add_child("Tea")
tree.children[0].add_child("Coffee")
tree.children[1].add_child("Soda")
tree.children[1].add_child("Water")
tree.traverse()
print(tree.search("Water"))
print(tree.search("Milk"))
tree.remove_child("Soda")
