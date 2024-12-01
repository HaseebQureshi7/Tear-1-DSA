#                                  -->   Matix    <--
#                           Simply a multi-Dimensional Array


# Search the given target in an 2D Array
# Approach
# using binary search after converting 2D into 1D Array

# TC -> O(LogN)
def searchIn2DArray(matrix, target):
    m, n = len(matrix), len(matrix[0])

    low, high = 0, m * n - 1

    while low <= high:
        mid = (low + high) // 2
        # Converting 2D into 1D array
        row, col = (
            mid // n,
            mid % n,
        )  # row, len(col) = midPoint // col, midPoint % len(col)

        if matrix[row][col] == target:
            return [row, col]
        if target < matrix[row][col]:
            high = mid - 1
        else:
            low = mid + 1

    return False


def setMatrixZeros(matrix):
    m, n = len(matrix), len(matrix[0])

    # taking fixed sized arrays for row and col
    row, col = [True]*m, [True]*n

    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 0:
                row[i] = False
                col[j] = False
    
    for i in range(len(row)):
        if row[i] == False:
            matrix[i] = [0]*n

    for j in range(len(col)):
        if col[j] == False:
            for k in range(m):
                matrix[k][j] = 0


    return matrix


def rotateImage(image):
    n = len(image)
    
    # Transposing the matrix
    for i in range(n):
        for j in range(i+1, n):
            image[i][j], image[j][i] = image[j][i],image[i][j]
    
    for i in range(n):
        image[i].reverse()

    return image