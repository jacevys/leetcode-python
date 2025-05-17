from typing import List, Optional
#
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        #
        array = []
        self.function(root, array)
        return array
#
    def function(self, root, array):
        if root:
            self.function(root.left, array)
            array.append(root.val)
            self.function(root.right, array)
#
    def inorderTraversal_2(self, root: Optional[TreeNode]) -> List[int]:
        array, stack = [], []

        while True:
            while root:
                stack.append(root)
                root = root.left

            if not stack:
                return array

            node = stack.pop()
            array.append(node.val)
            root = node.right
#
def main():
    ...
#
if __name__ == '__main__':
    main()
#
'''
2022.11.17
(1)failed
(2)checked
'''