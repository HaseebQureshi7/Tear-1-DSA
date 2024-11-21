# BINART TREE ---> NON LINEAR DS
#   BINARY SEARCH TREE


# Write a Binary Search Tree using Iteration <Better | Faster>
class TreeNode:
    def __init__(self, val, leftNode=None, rightNode=None):
        self.val = val
        self.left = leftNode
        self.right = rightNode


class BST:
    def __init__(self):
        self.root = None
        self.count = 0

    def add(self, val):
        newNode = TreeNode(val)
        if not self.root:
            self.root = newNode
            return

        temp = self.root
        while temp:
            if val == temp.val:
                return
            if val < temp.val:
                if not temp.left:
                    temp.left = newNode
                    self.count += 1
                temp = temp.left
            else:
                if not temp.right:
                    temp.right = newNode
                    self.count += 1
                temp = temp.right

    def delete(self, val):
        pass

    # O(logN)
    def contains(self, val):
        temp = self.root

        while temp:
            if val == temp.val:
                return True
            if val < temp.val:
                temp = temp.left
            else:
                temp = temp.right

        return False

    def length(self):
        return self.count + 1


# Write a Binary Search Tree using Recursion <Shorter | Complex>
class RecursiveBST:
    def __init__(self):
        self.root = None
        self.count = 0

    def add(self, root, val):
        if root is None:
            self.count += 1
            newRoot = TreeNode(val)
            self.root = newRoot
            return newRoot
        
        if val < root.val:
            root.left = self.add(root.left, val)
        if val > root.val:
            root.right = self.add(root.right, val)

        self.count += 1
        return root

    def delete(self, val):
        pass

    # O(logN)
    def contains(self, root, val):
        if not root:
            return False

        if root.val == val:
            return True
        if root.val > val:
            return self.contains(root.left, val)
        else:
            return self.contains(root.right, val)

    def length(self):
        return self.count + 1
