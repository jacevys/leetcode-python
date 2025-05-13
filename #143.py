# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        previous, current = None, slow

        while current:
            nxt = current.next
            current.next = previous
            previous = current
            current = nxt

        p1, p2 = head, previous

        while p2.next:
            n1 = p1.next
            p1.next = p2
            p1 = n1
            n2 = p2.next
            p2.next = p1
            p2 = n2
'''
2023.07.15
1.failed
'''