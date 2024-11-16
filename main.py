from general.problems import count_factors_optimized, is_prime, gcd, lcm
import arrays.problems
import recursion.problems
import hashing.problems as hash
import sorting.alg as sortingAlgos
import sorting.problems as sorting
import linked_list.DS as linkedListDs
import linked_list.problems as linkedListProblems
import stack.DS as stackDs
import stack.problems as stackProblems
import Queue.DS as queueDs


def main():
    k = 5
    emptyArray = []
    binaryArray = [1, 0, 1, 1, 0, 0, 0, 1, 0]
    ternaryArray = [1, 0, 1, 1, 0, 2, 0, 2, 0, 2, 2, 0, 1]
    sortedArray = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    unsortedArray = [1, 34, 15, 65, 44, 56, 86, 73, 45, 23, 31, 13]
    sortedArrayWithDuplicates = [1, 1, 2, 3, 4, 5, 5, 5, 6, 7, 7, 7, 8, 9, 0]
    reversedSortedArray = [7, 8, 9, 0, 1, 2, 3, 4, 5]
    unsortedArrayWithNegativeElements = [-1, 4, -23, 12, 5, 66, 74, -99, 10]

    lowerCaseString = "letter"
    lowerCaseString2 = "ettler"

    overlapping2DArray = [[1, 3], [2, 5], [1, 6], [5, 7], [7, 10]]
    nonOverlapping2DArray = [[1, 3], [3, 5], [6, 8], [9, 10], [10, 12]]

    headNode = linkedListDs.Node(1)
    n2 = linkedListDs.Node(2)
    n3 = linkedListDs.Node(3)
    n4 = linkedListDs.Node(4)

    headNode.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = None

    validParantheses = "[{()}]"
    invalidParantheses = "[{()]}"

    # print(arrays.problems.FindFrequencyOfKInArray(sortedArrayWithDuplicates, k))
    # res = arrays.problems.FindMinOfReverseSortedArrayWithLinearSearch(reversedSortedArray)
    # res = arrays.problems.FindMinOfReveredArrayWithBinarySearch(reversedSortedArray)
    # res = recursion.problems.printNumsInOrder(10)
    # res = recursion.problems.FindMinRecursion(reversedSortedArray)
    # res = recursion.problems.BinSearchWithRecursion(sortedArray, 99, 0, len(sortedArray) - 1)
    # res = hash.countFrequencyOfElsInArrayVanilla(sortedArrayWithDuplicates)
    # res = hash.countFrequencyOfElsInArray(sortedArrayWithDuplicates)
    # res = hash.countFrequencyOfArrayWithKnownConstraints(sortedArrayWithDuplicates)
    # res = hash.countFrequencyOfArrayWithNegativeConstraints(
    # unsortedArrayWithNegativeElements
    # )
    # res = hash.areAnagramsNaive(lowerCaseString, lowerCaseString2)
    # res = hash.areAnagramOptimized(lowerCaseString, lowerCaseString2)
    # res = hash.twoSumNaive(sortedArray, k)
    # res = hash.twoSumOptimized(sortedArray, k)
    # res = sortingAlgos.bubbleSort([7,8,19,0,5,4,15,9] )
    # res = sortingAlgos.selectionSort([7,8,19,0,5,4,15,9] )
    # res = sorting.segregate01(binaryArray)
    # res = sorting.segregate012(ternaryArray)
    # res = sortingAlgos.insertionSort(unsortedArray)
    # res = sortingAlgos.mergeSortedArrays([1,3,6,8,14,20,22], [2,4,5,7])
    # res = sortingAlgos.merge_sort(unsortedArray)
    # print(unsortedArray)
    # res = sortingAlgos.quickSort(unsortedArray, 0, len(unsortedArray) - 1)
    # res = sorting.twoSumInUnsortedArr([1, 7, -2, 5, -7, 2, -3, -7, 7, -2], 5)
    # res = sorting.twoSumWithDuplicates([1, 7, -2, 5, -7, 2, -3, -7, 7, -2], 5)
    # res = sorting.twoSumWithDuplicates2([1, 7, -2, 5, -7, 2, -3, -7, 7, -2], 5)
    # res = sorting.hasOverlap(overlapping2DArray)
    # res = sorting.canAttendMeetings(nonOverlapping2DArray)
    # res = sorting.mergeOverlappingIntervals([[1,5], [6,10], [11,12], [13,14]])
    # lList = linkedListDs.LinkedList()
    # lList.add(5)
    # lList.add(3)
    # lList.add(1)
    # lList.removeHead()
    # print(lList.contains(6))
    # lList.pop()
    # lList.addToFront(0)
    # lList.removeNode(1)
    # lList.printList()
    # print(lList.count)
    # newList = linkedListProblems.createListWithArray([1, 2, 3, 4, 5])
    # print(newList.value)
    # linkedListProblems.printReveredLinkedList(newList)
    # reversedList = linkedListProblems.reverseLinkedList(newList)
    # finalNode = newList.next.next.next
    # linkedListProblems.deleteNodeFromLinkedList(finalNode)
    # linkedListProblems.printLinkedList(newList)
    # res = linkedListProblems.returnMiddleNodeInLinkedListNAIVE(newList)
    # res = linkedListProblems.breakLinkedList(newList)
    # print(res[0].value, res[1].value)

    # print(linkedListProblems.hasCycle(headNode))
    # list1 = linkedListProblems.createListWithArray([1, 2, 3])
    # list2 = linkedListProblems.createListWithArray([4, 5, 6, 12,24,132,1])
    # res = linkedListProblems.removeNthFromReverse(headNode, 2)
    # res = linkedListProblems.mergeLinkedListsInAscendingOrder(list1, list2)
    # linkedListProblems.printLinkedList(res)
    # res = hash.threeSum([1,2,3,5,6,0,4],6)
    # print(res)

    # stack = stackDs.Stack()   # 3 Variations of Stack
    # stack = stackDs.LLStack()
    # stack = stackDs.DqStack()
    # stack = stackDs.MinStack()
    # stack.push(1)
    # stack.push(2)
    # stack.push(3)
    # stack.push(0)
    # stack.push(5)
    # for i in range(411):
    #     stack.push(i)

    # res = stack.peek()
    # print(res)
    # print(stack.pop())

    # stackSize = stack.size()
    # for i in range(stackSize):
    #     print(stack.pop())
    # stack.pop()

    # res = stackProblems.validParentheses("}}}}")
    # res = stackProblems.removeAdjacentDuplicates("aabbac")
    # res = stackProblems.nextWarmDay([73,74,76,71,69,79,73])
    # res = stackProblems.evaluatePrefix("*+-1234")
    # res = stackProblems.evaluatePrefix("-*+12354")
    # res = stackProblems.infixToPostfix("A+B*C+D/E")

    queue = queueDs.Queue()

    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.enqueue(4)

    res = queue.dequeue()

    print(res)


if __name__ == "__main__":
    main()
