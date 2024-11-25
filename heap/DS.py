#                       -->   HEAP / PRIORITY QUEUE
#               Heirarchial Data Structure (but looks like a Linear DS)


# Min Heap
# Smallest element will always be on top (ROOT WILL BE THE MIN VAL IN TREE)
class MinHeap:
    def __init__(self):
        self.data: list = []

    def __heapifyUp(self):
        currentIndex = len(self.data) - 1
        parentIndex = (currentIndex - 1) // 2  # Gives the parent index of child

        # Swapping current if its greater than its parent
        while currentIndex > 0 and self.data[parentIndex] > self.data[currentIndex]:
            self.data[parentIndex], self.data[currentIndex] = (
                self.data[currentIndex],
                self.data[parentIndex],
            )
            currentIndex = parentIndex
            parentIndex = (currentIndex - 1) // 2

    def __heapifyDown(self):
        # Sort from Top to Bottom
        heapLen = len(self.data)
        index = 0  # Starting from the 1st element
        leftChildIndex = (index * 2) + 1  # Gives left child index of the parent
        smallIndex = (index * 2) + 1

        while leftChildIndex < heapLen:
            rightChildIndex = (index * 2) + 2 # Gives the right child index
            # Checking if the rightEl is > leftEl, changing smallIndex to the min
            if rightChildIndex < heapLen and self.data[rightChildIndex] < self.data[smallIndex]:
                smallIndex = rightChildIndex
            # Checking if smallIndex of the upper 2 is smaller than parent. if yes, swap. 
            if self.data[smallIndex] < self.data[index]:
                self.data[index], self.data[smallIndex] = self.data[smallIndex], self.data[index]
                index = smallIndex
            else:
                return

    def add(self, val):
        self.data.append(val)
        self.__heapifyUp()  # Will Sort it automatically

    def remove(self):  # or pop()
        val = self.data[0]
        self.data[0] = self.data[-1]
        self.data.pop()
        self.__heapifyDown()
        return val

    def peek(self):
        if self.data:
            return self.data[0]
        else:
            raise Exception("Empty Heap!")

    def size(self):
        return len(self.data)

    def isEmpty(self):
        return len(self.data) == 0
