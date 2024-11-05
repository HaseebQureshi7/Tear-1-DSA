import collections

#   Hashing naturally sorts elements due to the fact that it puts the element to its corresponding index in the created array (cache).

# Count frequency of elements in an array
# using inbuilt Python Method -> Counter


# Best Case Time Complexity - O(1)
# Worst Case Time Complexity - O(N)
def countFrequencyOfElsInArray(arr: list) -> dict:
    cache = collections.Counter(arr)
    # print(cache[len(cache) - 3])
    return cache


# Count frequency of elements in an array without using inbuilt Counter Method


# Best Case Time Complexity - O(1)
# Worst Case Time Complexity - O(N)
def countFrequencyOfElsInArrayVanilla(arr: list) -> dict:
    cache = {}

    for el in arr:
        if el in cache:
            cache[el] = cache[el] + 1
        else:
            cache[el] = 1
    return cache


# Count frequency of elements in an array with given constraints
# Constraints -> 0 <= arr[i] <= 100

#  !!! Create a Solution by looking at the Constraints !!!


# Best Case Time Complexity - O(1)
# Worst Case Time Complexity - O(N)
def countFrequencyOfArrayWithKnownConstraints(arr: list) -> dict:
    cache = [
        0
    ] * 101  # creating an array and setting its size to 101 because a[i] <= 100

    def formatRawCache(rawCache: list) -> dict:
        formattedCache = {}
        for i in range(1, len(rawCache)):
            if rawCache[i] != 0:
                formattedCache[i] = rawCache[i]
        return formattedCache

    for i in arr:
        cache[i] = cache[i] + 1
    return formatRawCache(cache)  # Format the Array in a desirable fashion


# Count frequency of elements in an array with given constraints
# Constraints -> -100 <= arr[i] <= 100

#  !!! Create a Solution by looking at the Constraints !!!


# Best Case Time Complexity - O(1)
# Worst Case Time Complexity - O(N)
def countFrequencyOfArrayWithNegativeConstraints(arr: list) -> dict:
    cache = [
        0
    ] * 201  # creating an array and setting its size to 101 because a[i] <= 100

    def formatRawCache(rawCache: list) -> dict:
        formattedCache: dict = {}
        for i in range(1, len(rawCache)):
            if rawCache[i] != 0:
                formattedCache[i - 100] = rawCache[i]
        return formattedCache

    for el in arr:
        hashedIndex = el + 100
        cache[hashedIndex] = cache[hashedIndex] + 1
    return formatRawCache(cache)  # Format the Array in a desirable fashion


# Check if the 2 strings are Anagrams


# Naive Approach
# Best Case Time Complexity - O(2log(N)) -> O(log(N))
# Worst Case Time Complexity - O(2log(N)) -> O(log(N))
def areAnagramsNaive(s1: str, s2: str) -> bool:
    sortedAg1 = sorted(s1)  # Takes logN TC
    sortedAg2 = sorted(s2)
    return sortedAg1 == sortedAg2


# Check if the 2 strings are Anagrams
# Constraints -> s1, s2 are both lower case strings

# Optimized Approach (with Hashing)
# -> Approach
# ->    Will increment characters in one string's loop and subtract in the next one's
# ->    If the remaining cache is all 0s, its an Anagram, otherwise not.
# Best Case Time Complexity - O(1)
# Worst Case Time Complexity - O(3(N)) -> O(N)


def areAnagramOptimized(s1: str, s2: str) -> bool:
    if len(s1) != len(s2):
        return False  # This will take the Best Case TC to 0(1)

    cache = [
        0
    ] * 26  # not using 256 because constraints says "Only Lower Case Letters which are 26 (a-z)".

    def cacheCleaner(rawCache: list):
        for el in rawCache:
            if el != 0:
                return False
        return True

    # ->  2 SEPARATE LOOPS (LARGE FOOTPRINT BUT FAIRLY READABLE)
    for el in s1:
        charIndex = ord(el) - 97  # Starting from "a" whose ASCII code is 97
        cache[charIndex] = cache[charIndex] + 1
    for el in s2:
        charIndex = ord(el) - 97
        cache[charIndex] = cache[charIndex] - 1

    # ->  SINGLE LOOP (SMALL FOOTPRINT BUT NOT VERY READABLE)
    # for i in range(len(s1)):
    #     indexS1 = ord(s1[i]) - 97 # Starting from "a" whose ASCII code is 97
    #     indexS2 = ord(s2[i]) - 97
    #     cache[indexS1] = cache[indexS1] + 1
    #     cache[indexS2] = cache[indexS2] - 1
    return cacheCleaner(cache)


# Find if two of the elements in the array adds up to k and return True if found

# Naive Appraoch


# Best Case Time Complexity - O(N^2)
# Worst Case Time Complexity - O(N^2)
def twoSumNaive(arr, k):
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i] + arr[j] == k:
                return True
    return False


# Find if two of the elements in the array adds up to k and return True if found

# Optmized Appraoch


# Best Case Time Complexity - O(N)
# Worst Case Time Complexity - O(N)
def twoSumOptimized(arr, k):
    cache = set()

    for el in arr:
        elementToFind = k - el
        if (
            elementToFind in cache
        ):  # this is O(1) TC because of hashing (Reduces Overall TC)
            return (el, elementToFind)  # Returning indexes instead of True
        cache.add(
            el
        )  # Adding to cache after checking prevents one element to add up twice.
    return False


# Find if 3 of the elements in the array adds up to k and return all possible combinations

# Appraoch
# using 3 pointers, 1->left+1, 2->len(arr), 3->mid and move them back and forth


# Best Case Time Complexity - O(N^2)
# Worst Case Time Complexity - O(N^2)
def threeSum(arr, k):
    arr.sort()
    res = []

    for i in range(len(arr) - 2):
        low, high = i + 1, len(arr) - 1
        if i > 0 and arr[i] == arr[i - 1]:
            continue
        while low < high:
            sum = arr[i] + arr[low] + arr[high]
            if k > sum:
                low += 1
            elif k < sum:
                high -= 1
            else:
                res.append([arr[i], arr[low], arr[high]])
                while low < high and arr[low] == arr[low + 1]:
                    low += 1
                while low < high and arr[high] == arr[high - 1]:
                    high -= 1

                low += 1
                high -= 1

    return res
