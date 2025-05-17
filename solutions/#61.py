# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head

        n = 0
        p = head

        while p:
            n += 1
            p = p.next

        k = k % n
        if k == 0:
            return head

        p1, p2 = head, head

        for i in range(k):
            p2 = p2.next

        while p2 and p2.next:
            p1 = p1.next
            p2 = p2.next

        output = p1.next
        p1.next = None
        p2.next = head

        return output
'''
2023.10.09
1.failed
'''