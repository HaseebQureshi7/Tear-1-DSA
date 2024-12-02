#            FROM LEETCODE (NO TEST CASES IN MAIN FILE)

from collections import deque, defaultdict

#  0 1  2  3  4  5
# [1,12,-5,-6,50,3] k=4
#  2/4 = 0.5
#  51/4 = 12.5
#  42/4 = 10.5
# sub array, subset, sub sequence
# sub string, subset, sub sequence
# 100Mb -> Compression -> 10MB


# EASY LEETCODE QUESTION
def slidingWinAvg(arr, k):
    max_sum = curr_sum = sum(arr[:k])

    for i in range(k, len(arr)):
        curr_sum += arr[i]
        curr_sum -= arr[i - k]
        max_sum = max(curr_sum, max_sum)

    return max_sum / k


# O(N*K)
# O(N)
# 0 1 2 3 4 5 6 k = 3
# 0 1 2 3 4


# HARD LEETCODE QUESTION
def slidingWinMax(nums, k):
    # Initialize an empty list to store the results (the max values for each window)
    res = []

    # Initialize a deque to store the indices of potential maximum values
    q = deque()

    # Loop through each index of the array nums
    for i in range(len(nums)):
        # Check if the front of the deque is outside the current sliding window
        if q and q[0] <= i - k:
            # If the first element in the deque is outside the window, remove it
            q.popleft()

        # While the deque is not empty and the current number is larger than the number
        # at the index stored at the back of the deque, pop the back of the deque
        while q and nums[q[-1]] <= nums[i]:
            # This ensures that we maintain the deque in decreasing order
            q.pop()

        # Add the current index to the deque
        q.append(i)

        # Once we have processed enough elements (i.e., the window size is k)
        if i >= k - 1:
            # The front of the deque holds the index of the largest element in the current window
            res.append(nums[q[0]])

    # Return the list of maximum values for each sliding window
    return res


# O(N), O(1)


def kadanesMaxSum(arr):
    maxSum = float("-inf")
    currSum = 0

    for i in range(len(arr)):
        currSum += arr[i]
        maxSum = max(maxSum, currSum)
        # reset the window
        if currSum < 0:
            currSum = 0

    return maxSum


def hasDuplicates(s, start, end):
    map = defaultdict(int)
    for i in range(start, end + 1):
        map[s[i]] = map[s[i]] + 1

    for key, val in map.items():
        if val > 1:
            return True

    return False


# O(N*1), O(256)


def substrWithoutRepeatingChars(s):
    n = len(s)
    max_len = 0
    left = right = 0

    for right in range(n):
        while hasDuplicates(s, left, right):
            left += 1
        max_len = max(max_len, right - left + 1)

    return max_len


# DP
# Graphs
# Backtracking
# Bit manipulation
def minSizeSubArr(nums, target):
    minLen = float("inf")
    left = right = 0
    currTargetSum = 0

    for right in range(len(nums)):
        currTargetSum += nums[right]

        while currTargetSum >= target:
            windowSize = right - left + 1
            minLen = min(minLen, windowSize)
            currTargetSum -= nums[left]
            left += 1

    return 0 if minLen == float("inf") or None else minLen
