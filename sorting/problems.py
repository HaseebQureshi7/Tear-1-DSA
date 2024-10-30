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
