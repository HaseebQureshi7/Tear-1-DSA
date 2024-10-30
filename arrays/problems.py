#  Searching
# Linear search
# Binary search

# given an unsorted array and element k, return if an element exist


# Best Case Time Complexity - O(1)
# Worst Case Time Complexity - O(N)
def LinearSearch(arr, k):
    for elem in arr:
        if elem == k:
            return True

    return False


# Best Case Time Complexity - O(1)
# Worst Case Time Complexity - O(log(N))
def BinarySearch(arr, k):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == k:
            return True
        elif arr[mid] > k:
            right = mid - 1
        else:
            left = mid + 1

    return False


# Best Case Time Complexity - O(1)
# Worst Case Time Complexity - O(log(N))
def Sqroot(n):
    low, high = 1, n
    while low <= high:
        # mid = (low+high) // 2
        mid = low + ((high - low) // 2)
        val = mid * mid
        if val == n:
            return mid
        if val > n:
            high = mid - 1
        else:
            low = mid + 1
    return -1


# Best Case Time Complexity - O(1)
# Worst Case Time Complexity - O(log(N))
def FindFloorOfKInArr(arr, k):
    ans = -1
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = low + ((high - low) // 2)
        if arr[mid] == k:
            ans = mid
            high = mid - 1
        elif arr[mid] > k:
            high = mid - 1
        else:
            low = mid + 1

    return ans


# Best Case Time Complexity - O(1)
# Worst Case Time Complexity - O(log(N))
def FindCeilingOfKInArr(arr, k):
    ans, low, high = -1, 0, len(arr) - 1

    while low <= high:
        mid = low + ((high - low) // 2)
        if arr[mid] == k:
            ans = mid
            low = mid + 1
        elif arr[mid] > k:
            high = mid - 1
        else:
            low = mid + 1

    return ans


# Best Case Time Complexity - O(1)
# Worst Case Time Complexity - O(2log(N)) -> O(log(N))
def FindFrequencyOfKInArray(arr, k):
    start_index = FindFloorOfKInArr(arr, k)
    end_index = FindCeilingOfKInArr(arr, k)

    return 0 if start_index == -1 else end_index - start_index + 1


# Find Min of an Reversed Sorted Array


# Brute Force
# Best Case Time Complexity - O(1)
# Worst Case Time Complexity - O(N)
def FindMinOfReverseSortedArrayWithLinearSearch(arr):
    for i in range(len(arr)):
        if (
            arr[i] < arr[i + 1] and arr[i] < arr[i - 1]
        ):  # Breaks when given a sorted array
            return arr[i]


def FindLeastFromLeft(arr):
    left = 0
    right = len(arr) - 1
    min = -1
    while left <= right:
        mid = left + ((right - left) // 2)
        print("First el of LL -> ", arr[mid])
        if arr[mid] < arr[mid + 1] and arr[mid] < arr[mid - 1]:  # -> [9, mid<0>, 1]
            return arr[mid]
        elif arr[mid - 1] < arr[mid] and arr[mid + 1] > arr[mid]:
            right = mid - 1  # Go Left
            min = mid
        else:
            left = mid + 1  # Go Right
            min = mid
    return min


def FindLeastFromRight(arr):
    left = 0
    right = len(arr) - 1
    max = -1
    while left <= right:
        mid = left + ((right - left) // 2)
        print("First el of RR -> ", arr[mid])
        if arr[mid] < arr[mid + 1] and arr[mid] < arr[mid - 1]:  # -> [9, mid<0>, 1]
            return arr[mid]
        elif arr[mid - 1] < arr[mid] and arr[mid + 1] > arr[mid]:   
            left = mid + 1  # Go Right
            max = mid
        else:
            right = mid - 1  # Go Left
            max = mid
    return max


def FindMinOfReveredArrayWithBinarySearch(arr):
    left = FindLeastFromLeft(arr)
    right = FindLeastFromRight(arr)
    return (arr[(left + right) + 1])
