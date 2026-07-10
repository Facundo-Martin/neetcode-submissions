# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return
        
        # Step 1: Dump all nodes into an array
        nodes = []
        curr = head
        while curr:
            nodes.append(curr)
            curr = curr.next
            
        # Step 2: Use two pointers to rewire the nodes
        left, right = 0, len(nodes) - 1
        while left < right:
            nodes[left].next = nodes[right]
            left += 1
            
            # Check if pointers met in the middle
            if left == right:
                break
                
            nodes[right].next = nodes[left]
            right -= 1
            
        # Step 3: Crucial! Set the final node's next to None to prevent a cycle
        nodes[left].next = None

        
        # Input: LinkedList ??

        # Edge cases:
        # 1. 1 <= Length of the list <= 1000 -> If len == 1 then no need to reorder

        # Output: None!