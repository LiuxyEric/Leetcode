# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        pFast,pSlow = head, head
        while pFast and pFast.next:
            pFast, pSlow = pFast.next.next, pSlow.next
            if pFast is pSlow:
                pFast = head
                while pFast is not pSlow:
                    pFast, pSlow = pFast.next, pSlow.next
                return pFast
        return None
