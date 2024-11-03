class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class LinkedList:
    # Maintain a count and the head and tail when initializing
    def __init__(self):
        self.count = 0
        self.head = self.tail = None

    # Set both head & tail to None if no elements are found
    # O(1)
    def add(self, value):
        newNode = Node(value)
        self.count += 1
        # if self.count > 1:
        if self.head:
            self.tail.next = newNode
            self.tail = newNode
        else:
            self.head = self.tail = newNode

    # O(1)
    def addToFront(self, value):
        newNode = Node(value)
        self.count += 1
        if self.head:
            newNode.next = self.head
            self.head = newNode
        else:
            self.head = self.tail = newNode

    # O(1)
    def removeHead(self):
        if self.head:
            self.count -= 1
            newHead = self.head.next
            self.head = None
            self.head = newHead

    def listLength(self):
        return self.count

    # O(N)
    def printList(self):
        i = self.head
        listRes = ""
        while i:
            listRes += str(i.value) + " -> "
            i = i.next
        print(listRes + "None")

    # O(N)
    def contains(self, value):
        doesContain = False
        i = self.head
        while i:
            if i.value == value:
                return True
            i = i.next

        return doesContain

    # O(N)
    def pop(self):
        i = self.head
        newTail = None

        while i.next:
            newTail = i
            i = i.next
        self.tail = None
        newTail.next = None
        self.tail = newTail
        self.count -= 1

    # O(N)
    def removeNode(self, value):
        i = self.head
        lastNode = None
        # dyingNode = None
        while i:
            if i.value == value:
                if lastNode:
                    lastNode.next = i.next
                    i = None
                    self.count -= 1
                    return
                else:
                    newHead = i.next
                    i = None
                    self.head = newHead
                    self.count -= 1
                    return

            lastNode = i
            i = i.next
