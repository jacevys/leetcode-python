# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        vals = []

        for l in lists:
            while l:
                vals.append(l.val)
                l = l.next

        vals.sort()

        dummy = current = ListNode(val=0)

        for val in vals:
            current.next = ListNode(val=val)
            current = current.next

        return dummy.next
'''
2023.07.14
1.failed
'''
#