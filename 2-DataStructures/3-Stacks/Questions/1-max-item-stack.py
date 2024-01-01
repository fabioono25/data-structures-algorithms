# Return the maximum item of a stack in O(1) and O(n) space

from collections import deque

# using another stack
def getMax(inputStack):
  
  if (len(inputStack) == 1):
    return inputStack[0]
  
  maxStack = deque()
  maxStack.append(inputStack.pop())

  while len(inputStack) > 0:
    if maxStack[-1] < inputStack[-1]:
      maxStack.append(inputStack.pop())
    else:
      inputStack.pop()

  return maxStack[-1]

# using a variable
def getMax2(inputStack):
  maxItem = inputStack[0]
  for item in inputStack:
    if item > maxItem:
      maxItem = item

  return maxItem


# import Stack class from stacks.py
stack = deque()
stack.append(11)
stack.append(2)
stack.append(323)
stack.append(4)
stack.append(52)
stack.append(6)
print('Max: ', getMax(stack))
print(25*'-')
stack.append(11)
stack.append(2)
stack.append(323)
stack.append(4)
stack.append(52)
stack.append(6)
print('Max: ', getMax2(stack))