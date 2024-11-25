# Return the kth largest element in the arr (using heap<max heap>)
import heapq
from linked_list.DS import Node

# TC -> O(NLogK)
def kthLargertElement(arr, k):
    min_heap = []

    for el in arr:
        if len(min_heap) < k:
            heapq.heappush(min_heap, el)
        elif min_heap[0] < el:
            heapq.heappop(min_heap)
            heapq.heappush(min_heap, el)
    return min_heap[0]

# Return a single sorted list from the given K number of lists. 
def mergeKSortedLists(lists):
    min_heap = []
    for list in lists:
        if list:
            heapq.heappush(min_heap, (list.val, list))

    res = Node(-1)
    temp = res
    while min_heap:
        val, nd = heapq.heappop(min_heap)
        temp.next = Node(val)
        temp = temp.next
        if nd.next:
            heapq.heappush(min_heap, (nd.next.val, nd.next))

    return res.next