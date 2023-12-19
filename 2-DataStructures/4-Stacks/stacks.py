# Stack definition: a stack is a collection of elements that supports two principle operations: push and pop
# LIFO (Last In First Out)
# Operations: push, pop, peek, is_empty, size

class Stack:
    def __init__(self):
        self.stack = []

    # insert element at the end of the list. Time complexity: O(1)
    def push(self, data):
        self.stack.append(data)

    # remove the last element of the list. Time complexity: O(1)
    def pop(self):
        data = self.stack[-1]
        del self.stack[-1]
        return data

    # peek the last element of the list. Time complexity: O(1)
    def peek(self):
        return self.stack[-1]

    # check if the stack is empty. Time complexity: O(1)
    def is_empty(self):
        return self.stack == []

    # get the size of the stack. Time complexity: O(1)
    def stack_size(self):
        return len(self.stack)


# testing
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
print('Size: ', stack.stack_size())
print('Popped: ', stack.pop())
print('Size: ', stack.stack_size())
print('Peek: ', stack.peek())
print('Size: ', stack.stack_size())
