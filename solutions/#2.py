from typing import Optional
#
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
#
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        root = pointer = ListNode(val=0, next=None)

        while l1 or l2 or carry:
            v1 = v2 = 0

            if l1:
                v1 = l1.val
                l1 = l1.next
            if l2:
                v2 = l2.val
                l2 = l2.next

            summation = v1 + v2 + carry
            carry, remainder = (summation // 10), (summation % 10)

            pointer.next = ListNode(val=remainder, next=None)
            pointer = pointer.next

        return root.next
#
def creatLinkedList(linked_list_array):
    node_array = []
    pointer = None

    for digit in linked_list_array:
        node = ListNode(val=digit, next=None)
        node_array.append(node)

    for index, node in enumerate(node_array):
        if index == 0:
            pointer = node
        if (index + 1) >= len(node_array):
            break

        node.next = node_array[index + 1]

    return pointer
#
def printLinkedList(linked_list):
    output_string = ''

    while linked_list is not None:
        output_string += str(linked_list.val)

        if linked_list.next == None:
            break

        output_string += '->'
        linked_list = linked_list.next

    print(output_string)
#
def main():
    l1 = [9, 9, 9, 9, 9, 9, 9]
    l2 = [9, 9, 9, 9]
    linked_list_1 = creatLinkedList(l1)
    linked_list_2 = creatLinkedList(l2)
    printLinkedList(linked_list_1)
    printLinkedList(linked_list_2)
    solution = Solution()
    answer = solution.addTwoNumbers(linked_list_1, linked_list_2)
    printLinkedList(answer)
#
if __name__ == '__main__':
    main()
'''
2022.08.10:
(1)failed
(2)time: 2 hours 6 minutes
(3)checked

2022.09.25
(1)review
'''
#