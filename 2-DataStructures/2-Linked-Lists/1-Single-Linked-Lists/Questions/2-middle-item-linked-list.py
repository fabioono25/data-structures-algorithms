# question: find the middle item of a linked list in the most efficient way O(N)
# example: [1, 2, 3, 4, 5] -> 3

class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    # O(N) linear running time complexity
    # traversing using two pointers
    # when the fast pointer reaches the end of the list, the slow pointer is at the middle
    def get_middle_node(self):
        fast_pointer = self.head
        slow_pointer = self.head

        while fast_pointer.next_node and fast_pointer.next_node.next_node:
            fast_pointer = fast_pointer.next_node.next_node
            slow_pointer = slow_pointer.next_node

        return slow_pointer

    def insert(self, data):
        self.size = self.size + 1
        new_node = Node(data)

        if not self.head:
            self.head = new_node
        else:
            new_node.next_node = self.head
            self.head = new_node

    def traverse_list(self):
        actual_node = self.head

        while actual_node is not None:
            print("%d" % actual_node.data)
            actual_node = actual_node.next_node


class Node:
    def __init__(self, data):
        self.data = data
        self.next_node = None


if __name__ == "__main__":
    linked_list = LinkedList()
    linked_list.insert(1)
    linked_list.insert(2)
    linked_list.insert(3)
    linked_list.insert(4)
    linked_list.insert(5)
    linked_list.insert(6)
    linked_list.insert(7)
    linked_list.insert(8)
    linked_list.insert(9)
    linked_list.insert(10)

    middle_node = linked_list.get_middle_node()
    print(middle_node.data)