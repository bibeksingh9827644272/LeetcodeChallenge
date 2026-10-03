# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root):
        def height(node):
            # Empty tree has height 0
            if node is None:
                return 0

            # Find height of left subtree
            left = height(node.left)

            # If left subtree is unbalanced
            if left == -1:
                return -1

            # Find height of right subtree
            right = height(node.right)

            # If right subtree is unbalanced
            if right == -1:
                return -1

            # Difference in heights must be at most 1
            if abs(left - right) > 1:
                return -1

            # Return height of current node
            return max(left, right) + 1

        return height(root) != -1