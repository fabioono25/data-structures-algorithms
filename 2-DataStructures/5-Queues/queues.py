# Queues definition: a queue is a collection of elements that supports two principle operations: enqueue and dequeue
# First item in, first item out
# FIFO (First In First Out)
# Operations: enqueue, dequeue, is_empty, size

class Queue:
    def __init__(self):
        self.queue = []

    # is_empty: check if the queue is empty. Time complexity: O(1)
    def is_empty(self):
        return self.queue == []

    # enqueue: insert element at the end of the list. Time complexity: O(1)
    def enqueue(self, data):
        self.queue.append(data)

    # dequeue: remove the first element of the list. Time complexity: O(n) - Doubly-linked list would be O(1)
    def dequeue(self):
        if self.is_empty():
            return None

        data = self.queue[0]
        del self.queue[0]
        return data

    # size: get the size of the queue. Time complexity: O(1)
    def size(self):
        return len(self.queue)

    # peek: peek the first element of the list. Time complexity: O(1)
    def peek(self):
        return self.queue[0]

    # print the queue
    def print_queue(self):
        print(self.queue)


# testing
queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.print_queue()
print('Size: ', queue.size())
print('Dequeued: ', queue.dequeue())
queue.print_queue()
print('Size: ', queue.size())
print('Peek: ', queue.peek())
queue.print_queue()
print('Size: ', queue.size())
print('Is empty: ', queue.is_empty())
queue.dequeue()
queue.dequeue()
queue.dequeue()
print('Is empty: ', queue.is_empty())
