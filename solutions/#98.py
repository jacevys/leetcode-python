# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.valid(root, float('-inf'), float('inf'))


    def valid(self, root, min, max):
        if not root:
            return True

        if root.val >= max or root.val <= min:
            return False

        return self.valid(root.left, min, root.val) and self.valid(root.right, root.val, max)
'''
2023.08.03
1.failed
'''