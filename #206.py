# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(val=float('-inf'))

        while head:
            dummy.next, head.next, head = head, dummy.next, head.next

        return dummy.next

    def reverseList_2(self, head: Optional[ListNode]) -> Optional[ListNode]:
        previous = None
        current = head

        while current:
            nxt = current.next
            current.next = previous
            previous = current
            current = nxt

        return previous

    def reverseList_3(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head

        new_head = self.reverseList_3(head.next)
        head.next.next = head
        head.next = None

        return new_head
'''
2023.07.12
1.failed
'''
#