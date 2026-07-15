# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # Input:
        # 1D array, contains linked lists in asc order, signed integers -1000, 1000
        min_heap = []
        
        # 1. Push the head of each non-empty list into the heap
        for i, head_node in enumerate(lists):
            if head_node:
                heapq.heappush(min_heap, (head_node.val, i, head_node))
                
        dummy = ListNode(0)
        curr = dummy
        
        # 2. Extract min, connect it, and push its next element
        while min_heap:
            val, i, smallest_node = heapq.heappop(min_heap)
            
            curr.next = smallest_node
            curr = curr.next
            
            # If the popped node has a successor, push it to the heap
            if smallest_node.next:
                heapq.heappush(min_heap, (smallest_node.next.val, i, smallest_node.next))
                
        return dummy.next

        # Output
        # Sorted link list of merged linked lists