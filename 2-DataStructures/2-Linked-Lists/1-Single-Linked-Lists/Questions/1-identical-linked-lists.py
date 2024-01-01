# two linked lists are identical when same data and arrangement of data is the same. Write a function to check it.
# example: a = 1->2->3->4, b = 1->2->3->4 -> True
# example: a = 1->2->3->4, b = 1->2->3->5 -> False

from linked_list import LinkedList

class MyLinkedList(LinkedList):
    def areIdentical(self, listb):
        a = self.head
        b = listb.head
        while a != None and b != None:
            if a.data != b.data:
                return False
            a = a.next
            b = b.next
        return a == None and b == None

# Testing
if __name__ == "__main__":
    llist1 = MyLinkedList()
    llist2 = MyLinkedList()

    # The constructed linked lists are :
    # llist1: 3->2->1
    # llist2: 3->2->1
    llist1.push(1)
    llist1.push(2)
    llist1.push(3)
    llist2.push(1)
    llist2.push(2)
    llist2.push(3)

    # Function call
    if (llist1.areIdentical(llist2) == True):
        print("Identical ")
    else:
        print("Not identical ")
