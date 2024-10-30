import sys


# Print numbers from 1 to n without using iterators / loops
def printNumsInOrder(n, i=0):
    if i == n:
        return
    i = i + 1
    print(i)
    printNumsInOrder(n, i)


# Print nums in reverse order
def printNumsInReverse(n):
    if n == 0:
        return
    print(n)
    printNumsInReverse(n - 1)


# Find the min el in array
def FindMinRecursion(arr: list, min: int = sys.maxsize):
    if len(arr) > 0:
        finalEl = len(arr) - 1
        if arr[finalEl] < min:
            min = arr[finalEl]
        arr.pop()
        return FindMinRecursion(arr, min)
    return min


# Binary Search with Recursion
def BinSearchWithRecursion(arr, k, left, right):

    # Base Condition
    if left > right:
        return -1

    mid = left + (right - left) // 2
    if arr[mid] == k:
        return mid
    elif arr[mid] < k:  # arr=[1,2,4,5,7,8] k=7
        left = mid + 1
        return BinSearchWithRecursion(arr, k, left, right)
    else:
        right = mid - 1
        return BinSearchWithRecursion(arr, k, left, right)
