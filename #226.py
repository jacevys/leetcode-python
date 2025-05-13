# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is not None:
            left_tree = self.invertTree(root.left)
            right_tree = self.invertTree(root.right)
            root.left = right_tree
            root.right = left_tree

            return root
'''
2023.07.17
1.success
2.time: 5 minutes
'''