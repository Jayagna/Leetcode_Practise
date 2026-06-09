# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        top = head
        count = 1
        while top.next:
            count += 1
            top = top.next
        
        delnode = count - n

        if delnode == 0:
            head = head.next
        else:
            ptr = head
            prev = head
            for i in range(delnode):
                prev = ptr
                ptr = ptr.next

            prev.next = ptr.next
            ptr.next = None
        
        return head