# Segregation -> Sort an Binary Array of 0s and 1s only.

#  ---> 2 Pointer Technique


# Best Case Time Complexity - O(N)
# Worst Case Time Complexity - O(N)
# Space Complexity - O(1)
def segregate01(arr):
    left = 0
    right = len(arr) - 1

    while left < right:
        if arr[left] == 0:  # If 'left' points to a 0, it’s already in the correct place
            left += 1  # Move 'left' to the next element
        elif (
            arr[right] == 1
        ):  # If 'right' points to a 1, it’s already in the correct place
            right -= 1  # Move 'right' to the previous element
        else:  # If 'left' points to a 1 and 'right' points to a 0
            arr[left], arr[right] = arr[right], arr[left]  # Swap the elements
            left += 1  # Move 'left' forward
            right -= 1  # Move 'right' backward
    return arr  # Return the modified array


# Segregation2 -> Sort an Array of 0s, 1s and 2s only.

#  ---> 3 Pointer Technique


# Best Case Time Complexity - O(N)
# Worst Case Time Complexity - O(N)
# Space Complexity - O(1)
def segregate012(arr):
    left = 0
    mid = 0
    right = len(arr) - 1

    while mid <= right:
        if arr[mid] == 1:
            mid += 1
        elif arr[mid] == 0:
            arr[mid], arr[left] = arr[left], arr[mid]
            left += 1
            mid += 1
        else:
            arr[mid], arr[right] = arr[right], arr[mid]
            right -= 1
    return arr


# Two Sum in an Unsorted Array
# ex -> return any non repeating arr[indexs] in array which sums up to k

# Best Case Time Complexity - O(NLogN) + O(N) -> O(NLogN)
# Worst Case Time Complexity - O(N^2)
# Space Complexity - O(1)


# Approach
# Using Sorting alongside with 2 pointer.
def twoSumInUnsortedArr(arr: list, k: int) -> list:
    arr.sort()  # using Quick Sort, takes O(NlogN)
    left, right = 0, len(arr) - 1
    res = []

    while left <= right:  # using 2 Pointer, takes O(N)
        calc = arr[left] + arr[right]
        if calc == k:
            res.append([arr[left], arr[right]])
            left += 1
            right -= 1

        elif calc > k:
            right -= 1
        else:
            left += 1
    return res


# 2 Sum with With Duplicates in an Array
# My Implementation


def twoSumWithDuplicates(arr: list, k: int) -> list:
    arr.sort()  # using Quick Sort, takes O(NlogN)
    left, right = 0, len(arr) - 1
    cache = {}  # using caching to store duplicates.

    res = []

    while left <= right:  # using 2 Pointer, takes O(N)
        calc = arr[left] + arr[right]
        if calc == k:
            if (arr[left] not in cache) or (arr[right] not in cache):
                res.append([arr[left], arr[right]])
                cache[arr[left]] = 1
                cache[arr[right]] = 1
                left += 1
                right -= 1
            else:
                left += 1
                right -= 1

        elif calc > k:
            right -= 1
        else:
            left += 1
    return res


# 2 Sum with With Duplicates in an Array
# Teacher's Implementation


def twoSumWithDuplicates2(arr: list, k: int) -> list:
    arr.sort()  # using Quick Sort, takes O(NlogN)
    left, right = 0, len(arr) - 1
    res = []

    while left <= right:  # using 2 Pointer, takes O(N)
        calc = arr[left] + arr[right]
        if calc == k:
            res.append([arr[left], arr[right]])
            # Check for duplicates continously
            while left < right and arr[left] == arr[left + 1]:
                left += 1
            while left < right and arr[right] == arr[right - 1]:
                right -= 1

            left += 1
            right -= 1

        elif calc > k:
            right -= 1
        else:
            left += 1
    return res


# Find if the given Meetings are overlapping or not

# Approach
# Sort the intervals and compare the endTime and startTime of 2 side by side meetings.

# Best Case Time Complexity - O(NLogN) + O(N) -> O(NLogN)
# Worst Case Time Complexity - O(NLogN) + O(N) -> O(NLogN)
# Space Complexity - O(1)


def hasOverlap(intervals: list[list]) -> bool:
    # Sort by the 0th element of elements of interval array
    intervals.sort(key=lambda interval: interval[0])  # Takes O(NLogN)

    for i in range(1, len(intervals)):
        prevMeet = intervals[i - 1]
        nextMeet = intervals[i]

        # check if prevMeet's endTime is greater than nextMeet's start time.
        if prevMeet[1] > nextMeet[0]:
            return True

    return False


# Find if an Employee can attend all the given Meetings or not

# Approach
# Same as the previous problem

# Best Case Time Complexity - O(NLogN) + O(N) -> O(NLogN)
# Worst Case Time Complexity - O(NLogN) + O(N) -> O(NLogN)
# Space Complexity - O(1)


def canAttendMeetings(intervals: list[list]) -> bool:
    # Sort by the 0th element of elements of interval array
    intervals.sort(key=lambda interval: interval[0])  # Takes O(NLogN)

    # If there is no overlap, employee can attend all meetings
    for i in range(1, len(intervals)):
        prevMeet = intervals[i - 1]
        nextMeet = intervals[i]

        # check if prevMeet's endTime is greater than nextMeet's start time.
        if prevMeet[1] > nextMeet[0]:
            return False  # if any meeting overlaps, he can't attend all meetings.

    return True


# Merge Repeating Intervals

# Approach
# Check which intervals are overlapping and merge their start and end times.


def mergeOverlappingIntervals(intervals: list[list]) -> list:
    intervals.sort(key=lambda interval: interval[0])

    prev = intervals[0]
    res = []
    for i in range(1, len(intervals)):
        next = intervals[i]
        if prev[1] > next[0]:
            prev = [min(prev[0], next[0]), max(prev[1], next[1])]
        else:
            res.append(next)
            prev = next  # Move to the next interval if no overlapping is detected.

    res.append(prev)
    return res
