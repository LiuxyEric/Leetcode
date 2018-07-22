# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head or not head.next:
            return head

        n, pCur = 1, head
        while pCur.next:
            pCur = pCur.next
            n += 1
        pCur.next = head

        k = n - k % n
        while k != 0:
            pCur = pCur.next
            k -= 1
        head = pCur.next
        pCur.next = None
        return head 
