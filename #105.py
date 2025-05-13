# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None

        root = TreeNode(val=preorder[0])
        mid_index = inorder.index(preorder[0])

        root.left = self.buildTree(preorder[1:mid_index + 1], inorder[:mid_index])
        root.right = self.buildTree(preorder[mid_index + 1:], inorder[mid_index + 1:])

        return root
'''
2023.08.22
1.failed
'''

'''
preorder = [3, 9, 20, 15, 7], inorder = [9, 3, 15, 20, 7]

s1, done:
root=3, mid_index=1,
root.left=bt(preorder[1:2], inorder[:1])->call s2 = node(9), done
root.right=bt(preorder[2:], inorder[2:])->call s5 = node(20), done

return 3

s2(from s1, done):
pre=[9], in=[9], root=9, mid_index=0,
root.left=bt(preorder[1:1], inorder[:0])->call s3 = None
root.right=bt(preorder[1:], inorder[1:])->call s4 = None

tree:
   9
  / \
N     N

return root=9, back to s1

s3(from s2, done):
pre=[], in=[], return None, back to s2

s4(from s2, done):
pre=[], in=[], return None, back to s2

s5(from s1, done):
pre=[20, 15, 7], in=[15, 20, 7], root=20, mid_index=1
root.left=bt(preorder[1:2], inorder[:1])->call s6 = 15
root.right=bt(preorder[2:], inorder[2:])->call s9 = 7

tree:
   20
  /  \
15    7

return root=20, back to s1

s6(from s5, done):
pre=[15], in=[15], root=15, mid_index=0
root.left=bt(preorder[1:1], inorder[:0])->call s7 = None
root.right=bt(preorder[1:], inorder[1:])->call s8 = None

tree:
   15
  /  \
N      N

return root=15, back to s5

s7(from s6, done):
s8(from s6, done):

s9(from s5, done):
pre=[7], in=[7], root=7, mid_index=0
root.left=bt(preorder[1:1], inorder[:0])->call s10 = None
root.right=bt(preorder[1:], inorder[1:])->call s11 = None

tree:
   7
  / \
N     N

return root=7, back to s5

s10(from s9, done):
s11(from s9, done):
'''