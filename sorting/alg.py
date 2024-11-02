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


# Merge Sort


# Best Case Time Complexity - O(NLog(N))
# Worst Case Time Complexity - O(NLog(N))
# Space Complexity - O(N)
def merge(arr, low, mid, high):
    left = arr[low : mid + 1]
    right = arr[mid + 1 : high + 1]
    m, n = len(left), len(right)
    i = j = 0
    k = low

    # print("merging -> ", arr[low:high])

    while i < m and j < n:
        if left[i] < right[j]:
            arr[k] = left[i]
            k += 1
            i += 1
        else:
            arr[k] = right[j]
            j += 1
            k += 1

    while i < m:
        arr[k] = left[i]
        k += 1
        i += 1

    while j < n:
        arr[k] = right[j]
        k += 1
        j += 1

    return arr


def merge_sort_util(arr, low, high):
    # print(low, high)
    if low < high:
        mid = (low + high) // 2  # [1,3,2,7,0]
        merge_sort_util(arr, low, mid) # [1,3]
        merge_sort_util(arr, mid + 1, high) # [2,7,0]

        return merge(arr, low, mid, high)


def merge_sort(arr):
    return merge_sort_util(arr, 0, len(arr) - 1)

# Quick Sort

# Best Case Time Complexity - O(NLog(N))
# Worst Case Time Complexity - O(N^2)
# Space Complexity - O(1)

def partition(arr, left, right):
    pivot = arr[right]
    pI = left

    # print("prev -> ",arr)
    for i in range(left, right):
        if arr[i] <= pivot:
            arr[pI], arr[i] = arr[i], arr[pI]
            pI += 1
    arr[pI], arr[right] = arr[right], arr[pI]
    # print("after -> ", arr)
    return pI


def quickSort(arr, left, right):
    if left < right:
        partitionIndex = partition(arr, left, right)
        quickSort(arr, left, partitionIndex - 1)
        quickSort(arr, partitionIndex + 1, right)
