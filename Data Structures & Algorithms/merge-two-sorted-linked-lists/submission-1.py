# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        values = []
        
        # Dump all values from list1
        while list1:
            values.append(list1.val)
            list1 = list1.next
            
        # Dump all values from list2
        while list2:
            values.append(list2.val)
            list2 = list2.next
            
        # Sort the combined values
        values.sort()
        
        # Build a new linked list
        dummy = ListNode()
        current = dummy
        for val in values:
            current.next = ListNode(val)
            current = current.next
            
        return dummy.next