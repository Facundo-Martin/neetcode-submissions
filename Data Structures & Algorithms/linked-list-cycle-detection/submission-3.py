# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # If the list is empty or has only one node, there can't be a cycle
        if not head or not head.next:
            return False
        
        slow, fast = head, head

        # We must check 'fast' and 'fast.next' to prevent Null Pointer errors
        while fast and fast.next:
            slow = slow.next          # Moves 1 node
            fast = fast.next.next     # Moves 2 nodes
            
            # If they meet, a cycle exists!
            if slow == fast:
                return True
                
        # If 'fast' hits the end of the list (None), there is no cycle
        return False


        # Input:
        # LinkedList

        # Output
        # Boolean -> True if index != -1 else false 