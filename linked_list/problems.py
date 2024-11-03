from linked_list.DS import Node


# using only a node, create a static linked list.
def createListWithArray(arr):
    dummyNode = Node(-1)  # Wont be added to the Llist
    temp = dummyNode

    for i in arr:
        newNode = Node(i)
        temp.next = newNode
        temp = temp.next

    return dummyNode.next


# Print values of a LinkedList in reverse
# using recursion to fill the Python's call stack and resolve the last call first.
def printReveredLinkedList(head):
    if head == None:
        return

    # Last element will be handled first because of the Stack used in Python
    printReveredLinkedList(head.next)
    print(head.value)
