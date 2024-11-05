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


# Print a LinkedList
def printLinkedList(head):
    temp = head

    while temp:
        print(temp.value)
        temp = temp.next


# Print values of a LinkedList in reverse
# using recursion to fill the Python's call stack and resolve the last call first.
# BTC -> 0(N)
# WTC -> 0(N)
# SC => O(1)
def printReveredLinkedList(head):
    if head == None:
        return

    # Last element will be handled first because of the Stack used in Python
    printReveredLinkedList(head.next)
    print(head.value)


# Reverse an LinkedList with the given Head of the same


# Approach
# Point the first Node to Null and the rest to the previous Node
# BTC -> 0(N)
# WTC -> 0(N)
# SC => O(1)
def reverseLinkedList(head):
    temp = head
    prev = None

    while temp:
        next = temp.next  # next == 2 (starting from 1)
        temp.next = (
            prev  # Node 1's next will point to prev(Null or the Node saved in prev)
        )
        prev = temp  # Updating prev so the next Node's (next) can be set
        temp = next  # Updating temp to next value (2 here) so it can iterate

    return prev  # because temp contains the last processed Node (which will be its first now)


# Delete a given node (not value) in a LinkedList
# Approach
# Change the given Node's value to Node.next and its next to Node.next.next
# Won't work with the last Node due to no next Node.


# BTC -> 0(1)
# WTC -> 0(1)
# SC => O(1)
def deleteNodeFromLinkedList(node):
    if node.next:
        node.value = node.next.value
        node.next = node.next.next
    else:
        print("Last Node given, not removed!")


# NAIVE APPROACH
# Given a LinkedList, return the middle Node of the List
# Approach
# Go through the whole list and maintain a count and reiterate again until count/2 matches an Node's value
# BTC -> 0(2N) -> O(N)
# WTC -> 0(2N) -> O(N)
# SC => O(1)
def returnMiddleNodeInLinkedListNAIVE(head):
    temp = head
    count = 0

    while temp:
        count += 1
        temp = temp.next

    temp = head  # Reset the Head for reiteration
    mid = count // 2
    stopper = 0
    while temp:
        stopper += 1
        if stopper == mid:
            return temp.value
        temp = temp.next


# OPTIMIZED APPROACH
# Given a LinkedList, return the middle Node of the List

# Approach
# Use Slow - Fast Pointer Technique where 1 moves 1 step and another move 2 resulting --
# --in slow pointer pointing to the mid + 1


# BTC -> 0(N/2) -> O(N)
# WTC -> 0(N/2) -> O(N)
# SC => O(1)
def returnMiddleNodeInLinkedList(head):
    slowPointer = head
    fastPointer = head
    prev = None

    while fastPointer and fastPointer.next:
        prev = slowPointer
        slowPointer = slowPointer.next
        fastPointer = fastPointer.next.next
    return prev.value


# Given a LinkedList, break the LinkedList in the middle and return both new Lists.

# Approach


# BTC -> 0(N/2) -> O(N)
# WTC -> 0(N/2) -> O(N)
# SC => O(1)
def breakLinkedList(head):
    if not head or not head.next:
        # If there's only one node or no node, return the list as-is
        return head, None

    # Initialize slow and fast pointers
    slow = head
    fast = head

    # Move fast by 2 steps and slow by 1 step until fast reaches the end
    while fast and fast.next:
        prev = slow  # Save the previous node of slow
        slow = slow.next
        fast = fast.next.next

    # `slow` is now at the midpoint, so we break the list here
    second_half = slow
    prev.next = None  # Break the list into two parts

    return [head, second_half]  # Return the heads of the two halves




#               ---->    Floyd's Cycle Detection Algorithm     <----
#                   ---->    Tortoise and Hare Algorithm     <----
# Given a LinkedList, return True if the LinkedList contains a infinite cycle.

# Approach
# use slow-fast pointer technique to check if both slow & fast meet at some point


# BTC -> 0(N)
# WTC -> 0(N)
# SC => O(1)
def hasCycle(head):
    slow = fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False


# Given a head of a LinkedList, remove the nth node from reverse.

# Approach
# Use slow-fast pointer technique and increment fast by n and then increment both, -- 
# -- wherever fast stops, slow should be n-reversed LL 

# BTC -> O(2N) -> O(N)
# WTC -> O(2N) -> O(N)
# SC => O(1)
def removeNthFromReverse(head, n):
    dummyNode = Node(0)
    dummyNode.next = head
    slow = fast = dummyNode

    for _ in range(n): # use _ for variables which are not needed
        fast = fast.next

    while fast.next:
        fast = fast.next
        slow = slow.next

    slow.next = slow.next.next
    return dummyNode.next # always return the head which is connected to the final LL

# Given 2 LinkedLists, merge them in an acending order.

# Approach
# using 3 pointer, 2 for 2 LLs and one for new LL

# BTC -> O(2N) -> O(N)
# WTC -> O(2N) -> O(N)
# SC => O(1)
def mergeLinkedListsInAscendingOrder(head1, head2): # Doesnt work with Unsorted Lists 
    dNode = Node(0)
    temp1, temp2, temp3 = head1, head2, dNode

    while temp1 and temp2:
        if temp1.value < temp2.value:
            temp3.next = temp1
            temp1 = temp1.next
        else:
            temp3.next = temp2
            temp2 = temp2.next

        temp3 = temp3.next
    
    while temp1:
        temp3.next = temp1
        temp1 = temp1.next
        temp3 = temp3.next
    
    while temp2:
        temp3.next = temp2
        temp2 = temp2.next
        temp3 = temp3.next
    
    return dNode.next
