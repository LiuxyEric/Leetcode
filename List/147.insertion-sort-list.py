# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        if head is None or head.next is None:
            return head

        pReturn = ListNode(0)
        while head:
            pNode = pReturn
            pNext = head.next
            while pNode.next and pNode.next.val < head.val:
                pNode = pNode.next
            head.next = pNode.next
            pNode.next = head
            head = pNext
        return pReturn.next



        








