# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        len1 = self.getLength(l1)
        len2 = self.getLength(l2)
        maxlen = max(len1, len2)

        p1 = p2 = ListNode(0)
        while maxlen:
            p1.next = ListNode(0)
            p1 = p1.next
            if maxlen <= len1:
                p1.val += l1.val
                l1 = l1.next
            if maxlen <= len2:
                p1.val += l2.val
                l2 = l2.next
            maxlen -= 1
        p1 = p2
        while p1:
            p3 = p1.next
            while p3 and p3.val == 9:
                p3 = p3.next
            if p3 and p3.val > 9:
                while p1 != p3:
                    p1.val += 1
                    p1 = p1.next
                    p1.val -= 10
            else:
                p1 = p3
        return p2 if p2.val else p2.next



    def getLength(self, head):
        length = 0
        while head:
            length += 1
            head = head.next
        return length

