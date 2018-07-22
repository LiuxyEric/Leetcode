# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        def getLength(pNode):
            
            cnt = 0
            while pNode:
                cnt += 1
                pNode = pNode.next
            return cnt

        l1, l2 = getLength(headA), getLength(headB)
        if l1 > l2:
            pLong, pShort = headA, headB
            dist = l1 - l2
        else:
            pLong, pShort = headB, headA
            dist = l2 - l1
        while dist > 0:
            pLong = pLong.next
            dist -= 1
        pInter = None
        while pLong and pShort:
            if pLong == pShort:
                pInter = pLong
                break
            else:
                pLong = pLong.next
                pShort = pShort.next
        return pInter
