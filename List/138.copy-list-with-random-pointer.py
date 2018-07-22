# Definition for singly-linked list with a random pointer.
# class RandomListNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """

        pHead = head

        while pHead:
            pNode = RandomListNode(0)
            pNode.label = pHead.label
            pNode.next = pHead.next
            pHead.next = pNode
            pHead = pNode.next

        pHead = head
        while pHead:
            pNode = pHead.next
            if pHead.random is not None:
                pNode.random = pHead.random.next
            pHead = pNode.next
        
        pReturn = RandomListNode(0)
        pCloneNode, pHead = pReturn, head

        while pHead:
            pCloneNode.next = pHead.next 
            pHead.next = pHead.next.next
            pCloneNode = pCloneNode.next
            pHead = pHead.next
        return pReturn.next

