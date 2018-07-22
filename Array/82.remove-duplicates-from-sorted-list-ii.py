# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicate1s(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        pPrev, pCur = head, head.next
        while pCur :
            while pCur and pPrev.val == pCur.val:
                    pPrev.next = pCur.next
                    pCur = pCur.next
            if not pCur:
                return head
            pPrev = pCur
            pCur = pCur.next
        return head

    def deleteDuplicates(self, head):
        
        pR = ListNode(0)
        pPrev, pCur = pR, head
        while pCur:
            if pCur.next and pCur.next.val == pCur.val:
                val = pCur.val
                while pCur and pCur.val == val:
                    pCur = pCur.next
                pPrev.next = pCur
            else:
                pPrev.next = pCur
                pPrev = pCur
                pCur = pCur.next

        return pR.next



