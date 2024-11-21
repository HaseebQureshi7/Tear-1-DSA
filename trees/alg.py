#                             --> Depth First Search <--

# 3 Types of Tree Traversals Techniques with DFS
#   -> Preorder -> Root-Left-Right
#   -> Inorder -> Left-Root-Right
#   -> Postorder -> Left-Right-Root


# PREORDER  ->  Root-Left-Right
def preorder(root):
    if not root:
        return

    print(root.val)
    preorder(root.left)
    preorder(root.right)


# INORDER  ->  Left-Root-Right
def inorder(root):
    if not root:
        return

    inorder(root.left)
    print(root.val)
    inorder(root.right)


# POSTORDER  ->  Left-Right-Root
def postorder(root):
    if not root:
        return

    postorder(root.left)
    postorder(root.right)
    print(root.val)


# Find the min in a given tree
# Approach
# Keep going left until the tree runs of left nodes


# ATC -> O(LogN)
def findMin(root):
    if not root:
        return None

    temp = root
    while temp.left:
        temp = temp.left

    return temp.val


# Find the min in a given tree >> with Recursion
def findMinWithRecursion(root):
    if not root:
        return None

    if root.left == None:
        return root.val
    if root.left:
        return findMinWithRecursion(root.left)


# Find the max in a given tree
# Approach
# Keep going right until the tree runs of left nodes


# ATC -> O(LogN)
def findMax(root):
    if not root:
        return None

    temp = root
    while temp.right:
        temp = temp.right

    return temp.val


# Find the max in a given tree >> with Recursion
def findMaxWithRecursion(root):
    if not root:
        return None

    if not root.right:
        return root.val
    if root.right:
        return findMaxWithRecursion(root.right)


# Find the height of the given Binary Tree w/ Iteration
from collections import deque


def heightOfBinTreeIterative(root):
    if not root:
        return 0

    queue = deque([root])
    height = 0

    while queue:
        # Process all nodes at the current level
        level_size = len(queue)
        for _ in range(level_size):
            node = queue.popleft()
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        # Increment height after processing the current level
        height += 1

    return height


# Find the height of the given Binary Tree w/ Recursion
def heightOfBinTree(root):
    if not root:
        return 0
    #   --> Recursion calls can save their own length call internally <--
    #   --> but need adding something in the end <--
    leftHeight = heightOfBinTree(root.left)
    rightHeight = heightOfBinTree(root.right)
    # print(leftHeight, rightHeight)
    return 1 + max(leftHeight, rightHeight)


# Find if the given tree is balanced
def isBalanced(root):
    if not root:
        return True

    leftHeight = heightOfBinTree(root.left)
    rightHeight = heightOfBinTree(root.right)

    return (
        abs(leftHeight - rightHeight) <= 1
        and isBalanced(root.left)
        and isBalanced(root.right)
    )


# Count the leaves of the given tree (leaves are nodes w/o any child nodes)
def countLeaves(root):
    if not root:
        return 0

    if not root.left and not root.right:
        return 1

    return countLeaves(root.left) + countLeaves(root.right)


# Check if both given trees are identical are not
def areIdentical(root1, root2):
    if not root1 and not root2:
        return True

    if not root1 or not root2:
        return False

    if root1.val != root2.val:
        return False

    return areIdentical(root1.left, root2.left) and areIdentical(
        root1.right, root2.right
    )


# Invert the given binary tree (Pre-order)
def invertBinTree(root):
    if not root:
        return None

    root.left, root.right = root.right, root.left
    invertBinTree(root.left)
    invertBinTree(root.right)


#                         --> Breadth First Search <--


# BFS can be done using Level Order Traversal (each node is processed before moving to the next)
def levelOrderTraversal(root):
    if not root:
        return None

    q = deque()
    q.append(root)

    while q:
        nd = q.popleft()
        print(nd.val, end=" ")
        if nd.left:
            q.append(nd.left)
        if nd.right:
            q.append(nd.right)


# Print Levels of a Tree
def printLevels(root):
    if not root:
        return None

    q = deque()
    q.append(root)
    res = []

    while q:
        size = len(q)
        level = []

        for _ in range(size):
            node = q.popleft()
            if node:
                level.append(node.val)
                q.append(node.left)
                q.append(node.right)
        if level:
            res.append(level)
    return res


# Print the left view of the given Tree (if viewed from its left side)
# -- may contain elements from right side if left side is empty
def printLeftView(root):
    levels = printLevels(root)
    for level in levels:
        print(level[0], end=" -> ")


# Print the given tree's levels in the spiral order (zig zag)
def printSpiralOrder(root):
    if not root:
        return None

    q = deque()
    q.append(root)
    res = []
    leftToRight = False

    while q:
        size = len(q)
        level = []

        for _ in range(size):
            node = q.popleft()
            if node:
                level.append(node.val)
                q.append(node.left)
                q.append(node.right)
        if leftToRight:
            level.reverse()
        if level:
            leftToRight = not leftToRight
            res.append(level)
    return res


# Print the Spiral Order using Level Order Traversal
def spiralOrderWithLOT(root):
    levels = levelOrderTraversal(
        root
    )  # Not working! levelOrderTraversal needs to return something first!
    ltr = True
    for level in levels:
        if not ltr:
            level.reverse()
        print(level)
        ltr = not ltr


# Print the Vertical Order (if vertical/straight lines are drawn, print intersecting nodes)
from collections import defaultdict


def printVerticalOrder(root):
    if not root:
        return None

    res = defaultdict(list)  # using cache
    q = deque()
    q.append((root, 0))  # add root & horizontal distance

    while q:
        node, level = q.popleft()  # Returns 2 seperate objects from the tuple
        if node:
            res[level].append(node.val)
            q.append((node.left, level - 1))
            q.append((node.right, level + 1))

    # Returning Sorted Levels with Level Indexes
    # return sorted(res.items())

    # Returning Sorted Levels
    levels = []
    for item in sorted(res.items()):
        levels.append(item[1])
    return levels


# Print the Top View of the given tree
def printTopViewNaive(root):
    if not root:
        return None

    leftView = []
    rightView = []

    temp = root

    while temp.left:
        leftView.append(temp.left.val)
        temp = temp.left

    temp = root

    while temp.right:
        rightView.append(temp.right.val)
        temp = temp.right
    leftView.reverse()
    return (leftView, root.val, rightView)


def printTopView(root):
    if not root:
        return None

    # cache = defaultdict()
    cache = {}
    q = deque()
    q.append((root, 0))

    while q:
        # destructure the popped element
        node, horizDist = q.popleft()

        if node:
            if not horizDist in cache:
                cache[horizDist] = node.val
            q.append((node.left, horizDist - 1))
            q.append((node.right, horizDist + 1))

    return sorted(cache.items())


# Delete the given Node in the given Tree
def deleteFromTree(root, val):
    if not root:
        return None

    # Traverse the left or right subtree
    if root.val > val:
        root.left = deleteFromTree(root.left, val)  # Update the left subtree
    elif root.val < val:
        root.right = deleteFromTree(root.right, val)  # Update the right subtree
    else:
        # Node to delete found
        if not root.left:  # No left child
            return root.right
        elif not root.right:  # No right child
            return root.left
        else:
            # Node with two children
            min_val = findMin(
                root.right
            )  # Find the smallest value in the right subtree
            root.val = min_val  # Replace the current value with the successor's value
            root.right = deleteFromTree(
                root.right, min_val
            )  # Delete the successor node

    return root


def printFormattedTree(root, indent="", last=True):
    """
    Prints the binary tree in a pretty format resembling its structure.
    
    :param root: The root node of the binary tree.
    :param indent: Current indentation string for formatting.
    :param last: Boolean indicating if this is the last child in the current level.
    """
    if root is not None:
        # Print the current node with a branch
        print(indent, "`- " if last else "|- ", root.val, sep="")
        
        # Adjust the indentation for children
        indent += "   " if last else "|  "
        
        # Recursively print left and right children
        has_left = root.left is not None
        has_right = root.right is not None
        if has_left or has_right:
            printFormattedTree(root.left, indent, not has_right)
            printFormattedTree(root.right, indent, True)


#               >>> Leetcode questions


def maxDepth(root):
    if not root:
        return 0

    leftHeight = maxDepth(root.left)
    rightHeight = maxDepth(root.right)

    return 1 + max(leftHeight, rightHeight)