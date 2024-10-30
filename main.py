from general.problems import count_factors_optimized, is_prime, gcd, lcm
import arrays.problems
import recursion.problems
import hashing.problems as hash
import sorting.alg as sortingAlgos
import sorting.problems as sorting


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
    res = sortingAlgos.mergeSortedArrays([1,3,6,8,14,20,22], [2,4,5,7])
    print(res)


if __name__ == "__main__":
    main()
