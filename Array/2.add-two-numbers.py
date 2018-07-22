# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers1(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        pResult = ListNode(None)
        pCur = pResult
        flag = 0
        pl1, pl2 = l1, l2
        while pl1 and pl2:
            value = pl1.val + pl2.val + flag
            if value > 9:
                value = value % 10
                flag = 1
            else:
                flag = 0
            pCur.next = ListNode(value)
            pCur = pCur.next
            pl1 = pl1.next
            pl2 = pl2.next
        while pl1:
            value = pl1.val + flag
            if value > 9:
                value = value % 10 
                flag = 1
            else:
                flag = 0
            pCur.next = ListNode(value)
            pCur = pCur.next
            pl1 = pl1.next
        while pl2:
            value = pl2.val + flag
            if value > 9:
                value = value % 10
                flag = 1
            else:
                flag = 0
            pCur.next = ListNode(value)
            pCur = pCur.next
            pl2 = pl2.next
        if flag == 1:
            pCur.next = ListNode(1)
        return pResult.next
    
    def addTwoNumbers(self, l1, l2):
        pResult = ListNode(None)
        pCur, flag = pResult, 0
        while l1 or l2:
            val = flag
            if l1:
                val += l1.val
                l1 = l1.next
            if l2:
                val += l2.val
                l2 = l2.next
            flag, val = val / 10, val % 10
            pCur.next = ListNode(val)
            pCur = pCur.next

        if flag == 1:
            pCur.next = ListNode(1)

        return pResult.next

            
