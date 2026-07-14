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
        
        # Step 1: Create the mapping of {Old Node -> New Node}
        old_to_new = {}
        
        curr = head
        while curr:
            # Create a deep copy of the node (without pointers for now)
            old_to_new[curr] = Node(curr.val)
            curr = curr.next
            
        # Step 2: Connect the next and random pointers for the copies
        curr = head
        while curr:
            # Get the copied node
            copy = old_to_new[curr]
            
            # Connect the copy's next pointer to the copy of the next node
            copy.next = old_to_new.get(curr.next)
            
            # Connect the copy's random pointer to the copy of the random node
            copy.random = old_to_new.get(curr.random)
            
            curr = curr.next
            
        # Return the head of the brand-new list
        return old_to_new[head]

        