# Singly Linked Lists definition: A singly linked list is a collection of nodes that collectively form a linear sequence.
# Each node stores a reference to an object that is an element of the sequence, as well as a reference to the next node of the list.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return str(self.data)


class SingleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def insert(self, data):
        self.size += 1
        new_node = Node(data)

        if not self.head:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    # O(1) time complexity

    def inser_start(self, data):
        # self.num_nodes += 1
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            # self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1

    # O(n) time complexity
    def insert_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current_node = self.head

            # this is why it has O(n) time complexity
            while current_node.next is not None:
                current_node = current_node.next

            current_node.next = new_node
        self.length += 1

    # O(n) time complexity
    def insert_at(self, data, position):
        new_node = Node(data)
        if position == 0:
            self.inser_start(data)
        elif position == self.length:
            self.insert_end(data)
        else:
            current_node = self.head
            current_position = 0
            while current_position < position - 1:
                current_node = current_node.next
                current_position += 1

            new_node.next = current_node.next
            current_node.next = new_node
            self.length += 1

    def remove(self, data):
        if self.head is None:
            return None

        actual_node = self.head
        previous_node = None

        while actual_node is not None and actual_node.data != data:
            previous_node = actual_node
            actual_node = actual_node.next

        if actual_node is None:
            return

        if previous_node is None:
            self.head = actual_node.next
        else:
            previous_node.next = actual_node.next  # GC will remove the node

    # O(n) time complexity
    def traverse(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.data)
            current_node = current_node.next


# Test
my_list = SingleLinkedList()
my_list.inser_start(1)
my_list.inser_start("John")
my_list.inser_start(True)
my_list.insert_end(10.12)
my_list.insert_end("Hello")
my_list.insert_end(100)
my_list.insert_at("Middle", 3)
my_list.remove(100)
my_list.remove("John")
my_list.remove(True)
my_list.traverse()
