# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        pLess, pMore = ListNode(0), ListNode(0)
        pl, pm = pLess, pMore
        while head:
            if head.val < x:
                node = ListNode(head.val)
                pl.next = node
                pl = pl.next
            else:
                node = ListNode(head.val)
                pm.next = node
                pm = pm.next
            head = head.next
        pl.next = pMore.next
        return pLess.next
    
