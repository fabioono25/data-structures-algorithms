# define a single linked list class, with all the main methods
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    # push new node to the beginning of the linked list
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    # check if two linked lists are identical
    def areIdentical(self, listb):
        a = self.head
        b = listb.head
        while a != None and b != None:
            if a.data != b.data:
                return False
            a = a.next
            b = b.next
        return a == None and b == None
