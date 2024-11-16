# using built in deque
from collections import deque


class Queue:
    def __init__(self):
        self.data = deque()

    def enqueue(self, element):
        self.data.append(element)

    def dequeue(self):
        if len(self.data) == 0:
            raise Exception("Queue is empty!")
        return self.data.popleft()

    def peek(self):
        if len(self.data) == 0:
            raise Exception("Queue is empty!")
        return self.data[0]

    def length(self):
        return len(self.data)

    def isEmpty(self):
        return len(self.data) == 0
