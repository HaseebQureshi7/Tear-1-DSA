# Bubble sort O(N^2),O(1)
# natural order
# ascending order
# incrementing order
# non-decreasing order


# Bubble Sort


# Best Case Time Complexity - O(N)
# Worst Case Time Complexity - O(N^2)
# Space Complexity - O(1)
def bubbleSort(arr):
    sortingRange = len(arr) - 1
    isSorted = False

    while not isSorted:
        isSorted = True
        for i in range(sortingRange):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                isSorted = False
        sortingRange = (
            sortingRange - 1
        )  # The biggest el would be in the right place so discard the last el at the end of iteration.

    return arr


# Selection Sort


# Best Case Time Complexity - O(N^2)
# Worst Case Time Complexity - O(N^2)
def selectionSort(arr: list) -> list:
    arrLen = len(arr)

    for i in range(arrLen):
        minIndex = i  # Assuming the first el in arr is smallest

        for j in range(i + 1, arrLen):
            if arr[j] < arr[minIndex]:
                minIndex = j

        arr[i], arr[minIndex] = arr[minIndex], arr[i]
        # arr.pop(j)
    return arr


# Insertion Sort


# Best Case Time Complexity - O(N)
# Worst Case Time Complexity - O(N^2)
def insertionSort(nums: list) -> list:
    for i in range(1, len(nums)):
        j = i - 1
        key = nums[i]
        while j >= 0 and nums[j] > key:
            nums[j + 1] = nums[j]
            j -= 1
        nums[j + 1] = key

    return nums


# Merge 2 Sorted Arrays into a single sorted array

# Best Case Time Complexity - O(N+M)
# Worst Case Time Complexity - O(N+M)
# Space Complexity - O(N+M)
def mergeSortedArrays(arr1: list, arr2: list) -> list:
    n = len(arr1)
    m = len(arr2)
    i = 0  # Index/Pointer for arr1
    j = 0  # Index/Pointer for arr2
    sortedArr = []

    while i < n and j < m:
        if arr1[i] < arr2[j]:
            sortedArr.append(arr1[i])
            i += 1
        else:
            sortedArr.append(arr2[j])
            j += 1

    while i < n:
        sortedArr.append(arr1[i])
        i += 1

    while j < m:
        sortedArr.append(arr2[j])
        i += 1

    return sortedArr
