# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        pHead, ptail, ptailPrev = head, None, None
        while pHead and pHead.next:
            ptailPrev = pHead
            ptail = pHead.next
            pHead = pHead.next
        pHead = head
        pHead.next = ptail
        ptail.next = pHead.next
        pHead = pHead.next


            
