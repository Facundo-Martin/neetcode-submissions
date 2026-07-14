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

        new_nodes = {}
        curr = head

        while curr:
            new_nodes[curr] = Node(curr.val) # Copy new node to hashmap
            curr = curr.next

        curr = head
        while curr:
            copy = new_nodes[curr]

            copy.next = new_nodes.get(curr.next)
            copy.random = new_nodes.get(curr.random)

            curr = curr.next

        return new_nodes[head]

        