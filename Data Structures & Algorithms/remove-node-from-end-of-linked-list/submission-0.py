# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Create a dummy node pointing to head to handle edge cases
        # (e.g., removing the first node)
        dummy = ListNode(0, head)
        slow, fast = dummy, dummy
        
        # Step 1: Move fast pointer N steps ahead
        for _ in range(n):
            fast = fast.next
            
        # Step 2: Move both pointers until fast reaches the last node
        while fast.next:
            fast = fast.next
            slow = slow.next
            
        # Step 3: Delete the N-th node from the end
        slow.next = slow.next.next
        
        return dummy.next



        # Inputs:
        # 1. head: LinkedList, at least 1 node, values 0 - 100
        # 2. n: int, unsigned, 0 - sz (always in bounds)


        # Edge cases:
        # None


        # Outputs:
        # head: Head of modified linked list 