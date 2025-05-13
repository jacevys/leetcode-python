# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited = []

        while head:
            if head not in visited:
                visited.append(head)
            else:
                return True

            head = head.next

        return False

    def hasCycle_2(self, head: Optional[ListNode]) -> bool:
        fast, slow = head, head

        while fast and fast.next:
            fast, slow = fast.next.next, slow.next

            if fast == slow:
                return True

        return False
'''
2023.07.12
1.success
2.time: 5 minutes
'''
#