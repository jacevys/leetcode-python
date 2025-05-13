# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(root):
            if root == None:
                return 0

            left_h, right_h = dfs(root.left), dfs(root.right)

            if left_h < 0 or right_h < 0 or abs(left_h - right_h) > 1:
                return -1

            return max(left_h, right_h) + 1

        return dfs(root) >= 0
'''
2023.09.12
1.failed
2.time: 22 minutes
'''