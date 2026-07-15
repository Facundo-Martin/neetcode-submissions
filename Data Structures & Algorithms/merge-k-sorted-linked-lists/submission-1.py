# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # Input:
        # 1D array, contains linked lists in asc order, signed integers -1000, 1000
        dummy = ListNode(0)
        curr = dummy
        
        # Keep looping as long as at least one list head is not None
        while any(lists):
            smallest_val = float('inf')
            smallest_index = -1
            
            # Find the index of the minimum node currently at the front of the lists
            for i, node in enumerate(lists):
                if node and node.val < smallest_val:
                    smallest_val = node.val
                    smallest_index = i
            
            # Connect the smallest node and advance its list pointer
            curr.next = lists[smallest_index]
            curr = curr.next
            lists[smallest_index] = lists[smallest_index].next
            
        return dummy.next

        # Output
        # Sorted link list of merged linked lists