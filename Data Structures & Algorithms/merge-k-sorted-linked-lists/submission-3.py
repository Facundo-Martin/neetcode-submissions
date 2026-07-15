# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # Input:
        # 1D array, contains linked lists in asc order, signed integers -1000, 1000
        if not lists or len(lists) == 0:
            return None
            
        # Keep merging lists pairwise until only one list remains
        while len(lists) > 1:
            merged_lists = []
            
            # Step through lists two at a time
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i + 1] if (i + 1) < len(lists) else None
                
                # Merge the pair and add it to our new round of lists
                merged_lists.append(self.mergeTwoLists(l1, l2))
                
            lists = merged_lists
            
        return lists[0]
        
    # Helper function to merge exactly 2 sorted linked lists (O(1) auxiliary space)
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        curr = dummy
        
        while l1 and l2:
            if l1.val < l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next
            
        curr.next = l1 or l2
        return dummy.next
        # Output
        # Sorted link list of merged linked lists