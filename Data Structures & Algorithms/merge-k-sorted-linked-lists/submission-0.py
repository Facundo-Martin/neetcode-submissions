# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # Input:
        # 1D array, contains linked lists in asc order, signed integers -1000, 1000
        arr = []

        # 1. Collect all node values
        for l in lists:
            curr = l  # 'l' is already the head node of this linked list
            while curr:
                arr.append(curr.val)
                curr = curr.next
        
        # 2. Sort the collected values
        arr.sort()

        # 3. Rebuild a new sorted linked list
        dummy = ListNode(0)
        curr = dummy

        for val in arr:
            curr.next = ListNode(val)
            curr = curr.next
            
        return dummy.next

        # Output
        # Sorted link list of merged linked lists