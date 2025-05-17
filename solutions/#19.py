# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        counter = 0
        dummy = first = previous = ListNode(val=0)
        dummy.next = first.next = head
        dummy = dummy.next

        while dummy:
            counter += 1
            dummy = dummy.next

        target_index = counter - n

        for index in range(target_index):
            previous = head
            head = head.next

        previous.next = head.next

        return first.next

    def removeNthFromEnd_2(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = slow = fast = ListNode(val=0, next=head)

        for i in range(n):
            fast = fast.next

        while fast.next:
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next

        return dummy.next
'''
2023.07.14
1.success
2.time: 25 minutes
'''
#