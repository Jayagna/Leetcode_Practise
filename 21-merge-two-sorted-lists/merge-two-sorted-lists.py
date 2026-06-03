# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
        temp1 = list1
        temp2 = list2
        
        dummy = node = ListNode()

        while temp1 is not None and temp2 is not None:
            if temp1.val < temp2.val:
                node.next = temp1
                temp1 = temp1.next
                node = node.next
            else:
                node.next = temp2
                temp2 = temp2.next
                node = node.next

        while temp1 is not None:
            node.next = temp1
            temp1 = temp1.next
            node = node.next
        
        while temp2 is not None:
            node.next = temp2
            temp2 = temp2.next
            node = node.next
        
        return dummy.next
        