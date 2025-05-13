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
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy_node = ListNode(val=0, next=None)
        pointer = ListNode(val=0, next=None)

        if (list1 and list2) == None:
            return (list1 or list2)

        dummy_node.next = (list2 if list1.val >= list2.val else list1)
        pointer = dummy_node.next

        while (list1 or list2):
            if list1.val >= list2.val:
                temp = list2.next
                pointer.next = list2
                list2 = temp
            else:
                temp = list1.next
                pointer.next = list1
                list1 = temp

            pointer = pointer.next

            if (list1 and list2) == None:
                pointer.next = list1 or list2
                return dummy_node.next

    def mergeTwoLists_2(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        current = dummy = ListNode(val=0)

        while l1 and l2:
            if l1.val < l2.val:
                current.next = l1
                l1 = l1.next
            else:
                current.next = l2
                l2 = l2.next

            current = current.next

        current.next = l1 or l2

        return dummy.next
#
def main():
    list1 = [1, 2, 3]
    list2 = [1, 3, 4]
    linked_list1 = createLinkedList(list1)
    linked_list2 = createLinkedList(list2)
    showLinkedList(linked_list1)
    showLinkedList(linked_list2)
    solution = Solution()
    answer = solution.mergeTwoLists(linked_list1, linked_list2)
    showLinkedList(answer)
#
def createLinkedList(array):
    dummy_node = ListNode(val=0, next=None)
    pointer = ListNode(val=0, next=None)

    for index, digit in enumerate(array):
        new_node = ListNode(val=digit, next=None)

        if index == 0:
            dummy_node.next = new_node
        else:
            pointer.next = new_node

        pointer = new_node

    return dummy_node.next
#
def showLinkedList(linked_list):
    output_string = ''

    while linked_list:
        output_string += str(linked_list.val)
        output_string += '->'
        linked_list = linked_list.next

    output_string += 'None'

    print(output_string)
#
if __name__ == '__main__':
    main()
'''
2022.09.08
(1)success
(2)time: 1 hour 30 minutes
(3)checked
'''
#