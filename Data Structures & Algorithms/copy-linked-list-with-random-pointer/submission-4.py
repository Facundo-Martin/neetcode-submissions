"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        # Step 1: Weave the copied nodes directly after their originals
        # Original: A -> B
        # Weaved:   A -> A' -> B -> B'
        curr = head
        while curr:
            new_node = Node(curr.val)
            new_node.next = curr.next
            curr.next = new_node
            curr = new_node.next

        # Step 2: Wire up the random pointers for the copies
        curr = head
        while curr:
            if curr.random:
                curr.next.random = curr.random.next
            curr = curr.next.next

        # Step 3: Untangle the lists
        # Restore original next pointers and build cloned next pointers
        curr = head
        cloned_head = head.next
        
        while curr:
            copy = curr.next
            curr.next = copy.next  # Restore original link
            
            # Point copy.next to the next copy (if it exists)
            copy.next = copy.next.next if copy.next else None
            
            curr = curr.next       # Move to the next original node
            
        return cloned_head

        