# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head

        base = head
        pCur = base
        p1, p2 = ListNode(0), ListNode(0)
        pLess, pMore = p1, p2
        pHead = head.next
        while pHead:
            if pHead.val < base.val:
                pLess.next = pHead
                pLess = pLess.next
            elif pHead.val == base.val:
                pCur.next = pHead
                pCur = pCur.next
            else:
                pMore.next = pHead
                pMore = pMore.next
            pHead = pHead.next
        pLess.next = None
        pMore.next = None
        pCur.next = None
        p3 = self.sortList(p1.next)
        p4 = self.sortList(p2.next)
        if p3 is not None:
            p5 = p3
            while p5.next:
                p5 = p5.next
            p5.next = base
            pCur.next = p4
            return p3
        else:
            pCur.next = p4
        return base



        
            
