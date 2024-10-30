# Here are 10 easy binary search problems that will help you strengthen your understanding and application of binary search. These problems range from basic to slightly more challenging, covering different variations of binary search. Solving these will help you identify the kind of problems where binary search can be applied.

# 1. Binary Search on a Sorted Array
# Problem: Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.
# Concept: Classic binary search to find an element in a sorted array.


def FindN(arr, n) -> int:
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = left + ((right - left) // 2)
        if arr[mid] == n:
            return mid
        elif arr[mid] < n:
            left = mid + 1
        else:
            right = mid - 1
    return -1


def BinarySearchTemplate(arr, k) -> int | bool:
    # pointers
    left = 0
    right = len(arr) - 1

    # extract conditions separately
    def isEqual(n) -> int:
        if n == k:
            return True

    def isGreater(n) -> int:
        if n > k:
            return True

    # loop
    while left <= right:
        # Calculate Midpoint
        mid = left + ((right - left) // 2)

        # Conditions
        if isEqual(arr[mid]):
            return mid
        elif isGreater(arr[mid]):
            right = mid
        else:
            left = mid - 1
    return left


# 2. First Bad Version
# Problem: You are a product manager and currently leading a project. Unfortunately, one of the versions is bad, and since each version is built on the previous one, all subsequent versions are also bad. You want to find the first bad version.
# Concept: Use binary search to minimize API calls and find the first occurrence of a bad version.

# GIVEN
bad_version = 4  # Set the first bad version here


def isBadVersion(version):
    return version >= bad_version


# GIVEN


def FindBadVersion(n):
    left = 1  # Initialize left to 1 since versions start from 1
    right = n  # Initialize right to n

    while left < right:  # Continue while the search space is valid
        mid = left + (right - left) // 2  # Calculate the midpoint

        if isBadVersion(mid):  # Check if the mid version is bad
            right = mid  # If it's bad, search the left side (including mid)
        else:
            left = mid + 1  # If it's good, search the right side (excluding mid)

    return left  # When left == right, left points to the first bad version


# 3. Find Peak Element
# Problem: A peak element in an array is one that is greater than its neighbors. Find the index of any peak element.
# Concept: Binary search can be used to find a peak in logarithmic time by comparing mid and its neighbors.


def FindPeak(arr):
    left = 0
    right = len(arr) - 1

    while left < right:
        mid = left + (right - left) // 2

        # Check if mid is less than the next element
        if arr[mid] < arr[mid + 1]:
            left = mid + 1  # Move to the right
        else:
            right = mid  # Move to the left

    # At the end of the loop, left == right, and it points to a peak element
    return left  # or arr[left] if you want the peak value


# 4. Search Insert Position
# Problem: Given a sorted array and a target value, find the index where the target should be inserted to maintain the sorted order.
# Concept: Binary search helps in finding the correct position in logarithmic time.


# Approach
#   -> Use bin search and compare if the mid is smaller than k or larger.
def InsertTarget(arr, k):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == k:
            return mid
        elif arr[mid] < k:
            left = mid + 1
        else:
            right = mid - 1
    return left


# 5. Find the Square Root
# Problem: Implement the sqrt() function. Given a non-negative integer x, compute and return the square root of x.
# Concept: Binary search can be used to efficiently find the integer part of the square root.


# Approach
# Since finding the sqare root is sqrt * sqrt = n, I will use Bin Search to halve the array and check if the value is greater or smaller to move left or right
def SqrtWithBinSearch(n) -> int:
    left = 0
    right = n

    while left <= right:
        mid = left + (right - left) // 2
        possibleSqrt = mid * mid
        if possibleSqrt == n:
            return mid
        elif possibleSqrt < n:
            left = mid + 1
        else:
            right = mid - 1
    return -1


# 6. Find Minimum in Rotated Sorted Array
# Problem: A sorted array is rotated at some unknown pivot. Find the minimum element.
# Concept: Binary search can identify the unsorted portion of the array where the minimum element lies.


# Approach
# I will use Bin search and check the mid against leftmost and rightmost el to move left and right

def FindMinInRotatedSortedArr(arr) -> int:
    left = 0
    right = len(arr) - 1

    # while(left<right):
    for i in range(100):
        mid = left + (right - left) // 2
        # compare to the rightmost element
        if (arr[mid] > arr[right]):
            # Go right
            left = mid + 1
        else:
            right = mid
    return arr[left]


# Find higest el in array

# Approach 
# Reverse Engineer the FindMinElInArray

def FindMaxElInRotatedSortedArray(arr):
    left = 0
    right = len(arr) - 1

    while(left < right):
        mid = left + (right - left) // 2
        if (arr[mid] > arr[left]): # [5,6,0,1,2,3]
            left = mid
        else:
            right = mid
    return arr[left]


# Find an element in a Rotated Sorted Array



# 7. Find the Single Element in a Sorted Array
# Problem: In a sorted array where every element appears twice except for one, find the single element that appears only once.
# Concept: Binary search can help efficiently locate the element that appears once by exploiting the properties of pairs.

# 8. Guess Number Higher or Lower
# Problem: You are playing a guessing game with numbers between 1 and n. Given a guess function that returns -1 if the number is lower, 1 if higher, and 0 if correct, find the target number.
# Concept: Binary search narrows down the search space to quickly guess the correct number.


# Approach
# I will use Vanilla Bin Search and compare by calling the Guess Function to move left or right.
def FindGuessNumber(n) -> int | str:
    left = 0
    right = n

    def IsGuessCorrect(k):
        correctGuess = 7
        if k == correctGuess:
            return 0
        elif k < correctGuess:
            return -1
        else:
            return 1

    while left <= right:
        mid = left + (right - left) // 2
        if IsGuessCorrect(mid) == 0:
            return mid
        elif IsGuessCorrect(mid) == -1:
            left = mid + 1
        else:
            right = mid - 1
    return "Not Found"


# 9. Find the Position of an Element in an Infinite Sorted Array
# Problem: Given an infinite sorted array and a target value, return the index of the target or -1 if it is not present.
# Concept: First, you need to find the bounds using exponential search, then use binary search within those bounds.


# Approach
# I will use a loop to keep doubling the array's search size until the len(newArray) > n
def FindElInInfiniteArr(arr, k):
    left = 0
    right = 1

    # using another loop to exponentially increase the size of right until it is greater than k
    def ExponentiallyIncreaseRight(right, k):
        while k > right:
            right = right + right
            print("Increasing Right ^^", right)
        return right

    right = ExponentiallyIncreaseRight(right, k)

    while left <= right:
        print("Binary Search Started")
        mid = left + (right - left) // 2
        print("Mid -> ", mid)
        if arr[mid] == k:
            return mid
        elif arr[mid] < k:
            left = mid + 1
            print("Moving Right ->", left, right)
        else:
            right = mid - 1
            print("Moving Left ->", left, right)

    return -1


# 10. Find the Smallest Letter Greater than Target
# Problem: Given a circularly sorted array of characters and a target character, find the smallest letter that is greater than the target.
# Concept: Use binary search to find the smallest element greater than the given target.
# Key Focus Points While Solving These:
# Array should be sorted or have some kind of order.
# Focus on recognizing the "logarithmic" nature of the problem, which hints at binary search.
# Practice identifying edge cases, like the first or last element, duplicates, etc.
# Once you're comfortable, try variations like binary search on answers (applying binary search to find a minimum/maximum in a function or sequence).

# Solving these problems will solidify your binary search skills and help you recognize when it's the appropriate tool for a given problem.

k = 5
n = 9
emptyArray = []
sortedArray = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
unsortedArray = [1, 34, 15, 654, 44, 56, 86, 73, 45, 23, 231, 123]
sortedArrayWithDuplicates = [1, 1, 2, 3, 4, 5, 5, 5, 6, 7, 7, 7, 8, 9, 0]
rotatedSortedArray = [7, 8, 9, 0, 1, 2, 3, 4, 5]
longArr = [
    1,
    2,
    3,
    4,
    5,
    6,
    7,
    8,
    9,
    10,
    11,
    12,
    13,
    14,
    15,
    16,
    17,
    18,
    19,
    20,
    21,
    22,
    23,
    24,
    25,
    26,
    27,
    28,
    29,
    30,
    31,
    32,
    33,
    34,
    35,
    36,
    37,
    38,
    39,
    40,
    41,
    42,
    43,
    44,
    45,
    46,
    47,
    48,
    49,
    50,
]


# res = FindN(sortedArray, k) # Q1 -> Done
# res = FindBadVersion(n)  # Q2 -> Didn't understand
# res = FindPeak(reversedSortedArray)  # Q3 -> Partially Done
# res = InsertTarget(sortedArray, k)  # Q4 -> Done
# res = SqrtWithBinSearch(n)  # Q5 -> Done
# res = FindGuessNumber(n)  # Q6 ->
# res = FindElInInfiniteArr(longArr, n)  # Q7 -> Done
# res = FindMinInRotatedSortedArr(rotatedSortedArray)  # Q8 -> Done
res = FindMaxElInRotatedSortedArray(rotatedSortedArray)  # Q7a -> Done
print("Result -> ", res)
