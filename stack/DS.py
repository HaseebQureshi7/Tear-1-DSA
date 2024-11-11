# Write a Stack with Array (All methods must be O(1))
# Follows LIFO -> Last In, First Out
class Stack:
    def __init__(self):
        self.count = 0  # instantiate a count variable on Stack invocation.
        self.stackSize = 20
        self.data = [0] * self.stackSize  # Allocating a start stackSize

    def push(self, element):
        if self.count == self.stackSize:
            self.allocateMemory()
        self.data[self.count] = element
        self.count += 1

    def pop(self):
        if self.count == 0:
            raise Exception("Stack is Empty")
        if (
            self.count < self.stackSize // 4
        ):  # If count falls below the quarter of stackSize, half it.
            self.deallocateMemory()
        self.count -= 1
        return self.data[self.count]

    def peek(self):
        if self.count == 0:
            raise Exception("Stack is Empty")
        return self.data[self.count - 1]

    def size(self):
        return self.count

    def isEmpty(self):
        return False if self.count else True

    # Memory Alloction & Deallocation Methods
    def allocateMemory(self):  # Dynamic Memory Allocation
        self.stackSize *= 2
        newStackData = [0] * self.stackSize
        # copy the prev stack to the new one
        for i in range(self.count):
            newStackData[i] = self.data[i]
        self.data = newStackData

    def deallocateMemory(self):  # Dynamic Memory Deallocation
        self.stackSize //= 2
        newStackData = [0] * self.stackSize
        # copy the prev stack to the new one
        for i in range(self.count):
            newStackData[i] = self.data[i]
        self.data = newStackData


# Write a Stack with LinkedList
from linked_list.DS import LinkedList


class LLStack:
    def __init__(self):
        self.data = LinkedList()

    def push(self, element):
        self.data.addToFront(element)

    def pop(self):
        if self.isEmpty():
            raise Exception("Stack is Empty!")
        lastElement = self.data.head
        self.data.removeHead()
        return lastElement.value

    def peek(self):
        if self.isEmpty():
            raise Exception("Stack is Empty!")
        return self.data.head.value

    def size(self):
        return self.data.listLength()

    def isEmpty(self):
        return self.data.listLength() == 0


# Write a Stack with Deque (Built-in)
from collections import deque

class DqStack:
    def __init__(self):
        self.data = deque()

    def push(self, element):
        self.data.append(element)

    def pop(self):
        if self.isEmpty():
            raise Exception("Stack is Empty!")
        return self.data.pop()

    def peek(self):
        if self.isEmpty():
            raise Exception("Stack is Empty!")
        return self.data[-1]

    def size(self):
        return len(self.data)

    def isEmpty(self):
        return len(self.data) == 0


# ---> Modified Stack Implemention
# Write a MinStack (which returns the min val with O(1) TC)
# Approach
# Save the stack val alongside the min until that moment in a tuple
class MinStack:
    def __init__(self):
        self.count = 0  # instantiate a count variable on Stack invocation.
        self.stackSize = 20
        self.data = [None] * self.stackSize  # Allocating a start stackSize

    def push(self, element):
        if self.count == self.stackSize:
            self.allocateMemory()

        minTuple = (element, element)

        if self.count:
            lastMinVal = self.peek()[1]
            # minTuple = (element, lastMinVal if lastMinVal < element else element)
            #                               OR
            minTuple = (element, min(lastMinVal, element))

        self.data[self.count] = minTuple
        self.count += 1

    def pop(self):
        if self.count == 0:
            raise Exception("Stack is Empty")
        if (
            self.count < self.stackSize // 4 and self.count > 1
        ):  # If count falls below the quarter of stackSize, half it.
            self.deallocateMemory()
        self.count -= 1
        return self.data[self.count]

    def peek(self):
        if self.count == 0:
            raise Exception("Stack is Empty")
        return self.data[self.count - 1]

    def size(self):
        return self.count

    def isEmpty(self):
        return False if self.count else True

    # Memory Alloction & Deallocation Methods
    def allocateMemory(self):  # Dynamic Memory Allocation
        self.stackSize *= 2
        newStackData = [0] * self.stackSize
        # copy the prev stack to the new one
        for i in range(self.count):
            newStackData[i] = self.data[i]
        self.data = newStackData

    def deallocateMemory(self):  # Dynamic Memory Deallocation
        self.stackSize //= 2
        newStackData = [0] * self.stackSize
        # copy the prev stack to the new one
        for i in range(self.count):
            newStackData[i] = self.data[i]
        self.data = newStackData
