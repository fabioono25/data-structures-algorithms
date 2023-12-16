# doubly-linked lists definition: it is a list that has a head and a tail
# and each node has a pointer to the next node and the previous node
# the tail's next node is None and the head's previous node is None
# the head's previous node is None and the tail's next node is None

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    # add a node to the end of the list, so we have to manipulate the tail node in O(1) runtime
    def insert(self, value):
        newNode = Node(value)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            # the tail's next node is the new node
            self.tail.next = newNode
            # the new node's previous node is the tail
            newNode.prev = self.tail
            # the new node is the new tail
            self.tail = newNode
        self.length += 1
        return self

    # traversing the double linked lists in both directions
    def traverse_forward(self):
        current = self.head
        while current is not None:
            print(current.value)
            current = current.next

    def traverse_backward(self):
        current = self.tail
        while current is not None:
            print(current.value)
            current = current.prev


if __name__ == "__main__":
    myDoublyLinkedList = DoublyLinkedList()
    myDoublyLinkedList.insert(1)
    myDoublyLinkedList.insert(2)
    myDoublyLinkedList.insert(3)
    myDoublyLinkedList.insert(4)
    myDoublyLinkedList.insert(5)
    myDoublyLinkedList.insert(6)
    myDoublyLinkedList.insert(7)
    myDoublyLinkedList.insert(8)
    myDoublyLinkedList.insert(9)
    myDoublyLinkedList.insert(10)
    myDoublyLinkedList.traverse_forward()
    print("**********")
    myDoublyLinkedList.traverse_backward()
