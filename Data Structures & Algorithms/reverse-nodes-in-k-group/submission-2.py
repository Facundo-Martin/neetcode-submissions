# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # Step 1: Check if there are at least k nodes left
        curr = head
        for _ in range(k):
            if not curr:
                return head  # Less than k nodes, leave them as they are
            curr = curr.next
            
        # Step 2: Reverse the first k nodes of the list
        prev = None
        curr = head
        for _ in range(k):
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
            
        # Step 3: curr is now the head of the next group.
        # Recurse for the remaining list and link the tail of our 
        # current reversed group (which is 'head') to the result.
        if next_node:
            head.next = self.reverseKGroup(next_node, k)
            
        # Step 4: 'prev' is the new head of the reversed group
        return prev

        # Output:
        # Optional[ListNode] -> Head of the reversed linked list